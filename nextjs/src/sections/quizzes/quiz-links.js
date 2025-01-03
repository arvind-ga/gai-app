import React, {createContext, useContext, useEffect, useState} from 'react';
import { Box, Typography, Button, Container, Snackbar, Alert } from '@mui/material';
import { useRouter } from 'next/router';
import { useAuth } from '@/api/auth/auth-context';
import { checkQuizResponseExist, GenerateReport, downloadReport } from '@/api/endpoints';
import { checkReportExist, GetPmtStatus } from '@/api/endpoints';
import toast from 'react-hot-toast';

export default function QuizLinks() {
    const router = useRouter(); // Initialize the router object
    const [reportGenerating, setReportGenerating] = useState(false);
    const [reportExists, setReportExists] = useState(false);  // Define the reportExists state
    const [reportGenerated, setReportGenerated] = useState(false);
    const [submittedQuizzes, setSubmittedQuizzes] = useState({});
    const { userProfile, accessToken } = useAuth();

    // Verify if the report exists
    useEffect(() => {
        const verifyReportExistence = async () => {
            try {
                const response = await checkReportExist(userProfile?.username, accessToken);
                if (response?.message_code === "already_generated") {
                    setReportExists(true);
                } else {
                    setReportExists(false);
                }
            } catch (error) {
                toast.error("Error checking report existence. Please try again later.");
                console.error("Error checking report existence:", error);
            }
        };
    
        if (userProfile?.username && accessToken) {
            verifyReportExistence();
        }
    }, [userProfile, accessToken]);

    // Check quiz submission status for all quizzes
    useEffect(() => {
        const checkAllQuizzes = async () => {
            const quizIds = ['1', '2', '3', '4'];
            const statuses = {};

            for (const quizId of quizIds) {
                try {
                    const response = await checkQuizResponseExist(quizId, userProfile?.username, accessToken);
                    if (response?.message_code === "already_submitted") {
                        statuses[quizId] = true;
                    }
                } catch (error) {
                    console.error(`Error checking quiz ${quizId} submission status:`, error);
                }
            }

            setSubmittedQuizzes(statuses);
        };

        if (userProfile?.username && accessToken) {
            checkAllQuizzes();
        }
    }, [userProfile, accessToken]);
    
    const navigateTo = async (quizId, user_id) => {
        if (!quizId) {
            toast.error("Quiz ID is required to navigate.");
            return;
        }
        if (!user_id) {
            toast.error("Please complete your profile to give quiz tests");
            return;
        }
        try {
            const response = await checkQuizResponseExist(quizId, userProfile?.username, accessToken);
            console.log("Quiz response status", response)
            if (response.message_code === "already_submitted") {
                toast.success("You have already submitted this quiz:");
            } else {
                router.push(`/quiz?id=${quizId}&user_id=${user_id}`);
            }
        } catch (error) {
            toast.error("Failed to fetch quiz submission status. Please try again.");
            console.error("Error checking quiz submission status:", error);
        }
    };

    const handleGenerateReport = async () => {
        if (reportExists) {
            toast.info("Your report is already generated. Please download it.");
            return;
        }

        setReportGenerating(true);
        try {
            const [response1, response2, response3] = await Promise.all([
                checkQuizResponseExist("1", userProfile?.username, accessToken),
                checkQuizResponseExist("2", userProfile?.username, accessToken),
                checkQuizResponseExist("3", userProfile?.username, accessToken),
            ]);
            if (!(  response1?.message_code === "already_submitted" &&
                    response2?.message_code === "already_submitted" &&
                    response3?.message_code === "already_submitted"
                )
            ) {
                toast.error("Please complete all quizzes to generate the report.");
                return;
            }
            await GenerateReport(userProfile?.username, accessToken);
            setReportExists(true);
            toast.success("Report generated successfully. You can now download it.");
        } catch (error) {
            toast.error("Failed to generate report. Please try again.");
            console.error("Error while generating report:", error);
        } finally {
            setReportGenerating(false);
        }
    };

    const handleDownloadReport = async () => {
        try {
            const paymentStatus = await GetPmtStatus(userProfile?.username, accessToken);
            if (paymentStatus?.report_pmt_status) {
                await downloadReport(userProfile?.username, accessToken);
                toast.success("Report downloaded successfully.");
            } else {
                const session_booking_id= ""
                const feature = "report"
                toast.error("Payment required to download the report. Redirecting...");
                router.push(`/checkout?session_booking_id=${session_booking_id}&feature=${feature}`);
            }
        } catch (error) {
            toast.error("Failed to verify payment status. Please try again.");
            console.error("Error checking payment status:", error);
        }
    };

    return (
        <Container maxWidth="sm" sx={{ textAlign: 'center', marginTop: 5 }}>
            <Typography variant="h4" component="h1" gutterBottom>
                Assessment Quiz Links
            </Typography>
            <Box
                sx={{
                    display: 'flex',
                    flexDirection: 'column',
                    gap: 2,
                    padding: 3,
                    border: '1px solid #ccc',
                    borderRadius: 2,
                    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
                }}
            >
                {['1', '2', '3', '4'].map((quizId) => (
                    <Button
                        key={quizId}
                        variant="contained"
                        color={submittedQuizzes[quizId] ? 'info' : 'primary'}
                        onClick={() => navigateTo(quizId, userProfile?.username)}
                        sx={{
                            textTransform: 'none',
                            padding: '10px',
                            backgroundColor: submittedQuizzes[quizId] ? '#90caf9' : undefined,
                            color: submittedQuizzes[quizId] ? '#fff' : undefined,
                        }}
                    >
                        {`Quiz Test ${quizId} (${quizId === '3' ? '45 Min' : '30 Min'})`}
                        {quizId === '4' ? ': Optional' : ''}
                    </Button>
                ))}
                <Button
                    variant="contained"
                    color="secondary"
                    onClick={handleGenerateReport}
                    disabled={reportGenerating || reportExists}
                    sx={{ textTransform: 'none', padding: '10px', marginTop: 2 }}
                >
                    {reportGenerating ? 'Generating Report...' : 'Generate Report'}
                    </Button>
                        {reportExists && (
                            <Button
                                onClick={handleDownloadReport}
                                variant="outlined"
                                color="success"
                                sx={{ textTransform: 'none', padding: '10px', marginTop: 2 }}
                            >
                                Download Report
                    </Button>
                )}
            </Box>
        </Container>
    );
}
