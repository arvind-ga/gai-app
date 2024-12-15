import React, { useState } from 'react';
import { Box, Typography, Button, Container, Snackbar, Alert } from '@mui/material';
import { useRouter } from 'next/router';
import { useAuth } from '@/api/auth/auth-context';
import { GenerateReport } from '@/api/endpoints';
import { downloadReport} from "@/api/endpoints";

export default function QuizLinks() {
    const router = useRouter(); // Initialize the router object
    const [reportGenerating, setReportGenerating] = useState(false);
    const [reportGenerated, setReportGenerated] = useState(false);
    const { userProfile, accessToken } = useAuth();

    const navigateTo = (quizId) => {
        if (quizId) {
            router.push(`/quiz?id=${quizId}`);
        } else {
            console.error("Quiz ID is required to navigate");
        }
    };

    const handleGenerateReport = async () => {
        setReportGenerating(true);
        try {
            console.log('Generating Student Report');
            // const response = await GenerateReport(userProfile, accessToken);
            const response = await GenerateReport(userProfile.username, accessToken);
            console.log('Report generated successfully:', response);
            setEditMode(false); // Exit edit mode on success
        } catch (error) {
            console.error('Error while generating report:', error);
            setReportGenerating(false);
            // Optionally show a Snackbar with error information
        }

        // Simulate report generation with a delay
        setTimeout(() => {
            setReportGenerating(false);
            setReportGenerated(true);
        }, 10000); // Simulate 10-second delay
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
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => navigateTo('1')} // Navigate to Quiz Test 1
                    sx={{ textTransform: 'none', padding: '10px' }}
                >
                    Quiz Test 1 (30 Min)
                </Button>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => navigateTo('2')} // Navigate to Quiz Test 2
                    sx={{ textTransform: 'none', padding: '10px' }}
                >
                    Quiz Test 2 (30 Min)
                </Button>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => navigateTo('3')} // Navigate to Quiz Test 3
                    sx={{ textTransform: 'none', padding: '10px' }}
                >
                    Quiz Test 3 (45 Min)
                </Button>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => navigateTo('4')} // Navigate to Quiz Test 4
                    sx={{ textTransform: 'none', padding: '10px' }}
                >
                    Quiz Test 4 (30 Min): Optional
                </Button>
                <Button
                    variant="contained"
                    color="secondary"
                    onClick={handleGenerateReport}
                    disabled={reportGenerating}
                    sx={{ textTransform: 'none', padding: '10px', marginTop: 2 }}
                >
                    Generate Report
                </Button>
                {reportGenerated && (
                    
                    <Button
                        onClick={() => downloadReport(userProfile?.username)} 
                        variant="outlined"
                        color="success"
                        sx={{ textTransform: 'none', padding: '10px', marginTop: 2 }}
                        //href="/path-to-report.pdf" // Replace with the actual report file path
                        download
                    >
                        Download Report
                    </Button>
                )}
            </Box>
            <Snackbar
                open={reportGenerating}
                autoHideDuration={10000}
                onClose={() => setReportGenerating(false)}
                anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
            >
                <Alert severity="info" sx={{ width: '100%' }}>
                    Your report is being generated. Download after 5-10 minutes.
                </Alert>
            </Snackbar>
        </Container>    
    );
}
