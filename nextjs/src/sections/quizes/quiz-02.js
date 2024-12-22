import toast from "react-hot-toast";
import React, { useEffect, useState } from 'react';
import { useQuery } from 'react-query';
import { useRouter } from 'next/router';
import {
    Box,
    Button,
    Card,
    CardContent,
    CardHeader,
    CircularProgress,
    Container,
    FormControlLabel,
    Grid,
    Radio,
    RadioGroup,
    TextField,
    Typography,
} from '@mui/material';
import { deepPurple, green, red } from '@mui/material/colors';
import Avatar from '@mui/material/Avatar';
import { fetchQuiz, submitQuizResponse, getProfile } from '@/api/endpoints';
import Loading from '@/components/loading';
import { useAuth } from '@/api/auth/auth-context';


//const initialId = '1';
const QuizPage = ({ quiz_id }) => {
    console.log("Entered in QuizPage");
    const router = useRouter();
    const { accessToken } = useAuth();
    const [responses, setResponses] = useState({});
    const [submissionMessage, setSubmissionMessage] = useState('');
    const [quiz, setQuiz] = useState(null);
    const [incompleteQuestions, setIncompleteQuestions] = useState([]);

    const {
        data: user,
        isLoading: isUserLoading,
        isError: isUserError,
    } = useQuery('userProfile', () => getProfile(accessToken), {
        enabled: !!accessToken,
    });

    console.log("Fetching quiz with quiz id", quiz_id);
    // const {
    //     data: quizData,
    //     isLoading: isQuizLoading,
    //     isError: isQuizError,
    // } = useQuery(['quiz', quiz_id], () => fetchQuiz(quiz_id, user?.username, accessToken), {
    //     enabled: !!quiz_id,
    //     onSuccess: (data) => setQuiz(data),
    // });
    const { data: quizData, 
        isLoading: isQuizLoading,
        isError: isQuizError, } = useQuery(
        ['quiz', quiz_id],
        () => fetchQuiz(quiz_id, user?.username, accessToken),
        { enabled: !!quiz_id && !!user?.username,
            onSuccess: (data) => setQuiz(data),
         }
    );
    console.log("Fetched quiz with quiz id", quiz_id);

    const handleSubmit = async () => {
        if (!quiz) return;

        // Find unanswered questions
        const unanswered = quiz.questions
            .filter((question) => !responses[question.id])
            .map((q) => q.id);

        if (unanswered.length > 0) {
            toast.error("Please answer all questions before submitting.");
            setIncompleteQuestions(unanswered); // Highlight incomplete questions
            return;
        }

        setIncompleteQuestions([]); // Clear any previous highlights

        const submissionData = {
            username: user?.username || "",
            email: user?.email || "",
            user_id: user?._id || "",
            mobile_number: user?.mobile_number || "",
            quizId: quiz?.id || quiz_id,
            responses,
        };

        try {
            const result = await submitQuizResponse(submissionData, accessToken);
            toast.success("Submission successful!");
            setTimeout(() => {
                router.push("/quiz-links");
            }, 1000);
            console.log("Submission successful:", result);
        } catch (error) {
            console.error("Error submitting quiz response:", error);
            toast.error("Failed to submit quiz, please try again!");
            setSubmissionMessage(
                "Failed to submit quiz. Please check your answers or try again."
            );
        }
    };

    if (isUserLoading || isQuizLoading) return <Loading />;
    if (isUserError || isQuizError) return <Typography>Error loading data.</Typography>;

    return (
        <Container maxWidth="md" sx={{ marginTop: 5 }}>
            {/* User Details Card */}
            <Card sx={{ mb: 4, borderRadius: '16px', boxShadow: 3, padding: 3 }}>
                <CardHeader
                    title={<Typography variant="h4">Quiz: {quiz?.id.charAt(0) || "Loading..."}</Typography>}
                />
                <CardContent>
                    <Grid container spacing={3}>
                        <Grid item xs={12} sm={6}>
                            <Typography variant="body2">
                                <strong>Name:</strong> {user?.full_name || 'N/A'}
                            </Typography>
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <Typography variant="body2">
                                <strong>Email:</strong> {user?.email || 'N/A'}
                            </Typography>
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <Typography variant="body2">
                                <strong>Standard:</strong> {user?.standard || 'N/A'}
                            </Typography>
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <Typography variant="body2">
                                <strong>Medium:</strong> {user?.medium || 'N/A'}
                            </Typography>
                        </Grid>
                    </Grid>
                </CardContent>
            </Card>

            {/* Quiz Section */}
            <Card sx={{ borderRadius: "16px", boxShadow: 3 }}>
                <CardHeader title={<Typography variant="h4">Quiz Questions</Typography>} />
                <CardContent>
                    {quiz.questions.map((question) => (
                        <Box
                            key={question.id}
                            sx={{
                                marginBottom: 4,
                                padding: 4,
                                border: `2px solid ${
                                    incompleteQuestions.includes(question.id) ? red[500] : "#e0e0e0"
                                }`,
                                borderRadius: "8px",
                                backgroundColor: "#f9f9f9",
                            }}
                        >
                            <Typography variant="h6" sx={{ marginBottom: 2 }}>
                                {question.question}
                            </Typography>
                            <RadioGroup
                                value={responses[question.id] || ""}
                                onChange={(e) =>
                                    setResponses({ ...responses, [question.id]: e.target.value })
                                }
                            >
                                {question.options.map((option, index) => (
                                    <FormControlLabel
                                        key={index}
                                        value={option}
                                        control={<Radio />}
                                        label={option}
                                    />
                                ))}
                            </RadioGroup>
                        </Box>
                    ))}

                    <Button
                        variant="contained"
                        color="primary"
                        onClick={handleSubmit}
                        fullWidth
                        sx={{ mt: 3 }}
                    >
                        Submit Quiz
                    </Button>
                </CardContent>
            </Card>

            {/* Submission Message */}
            {submissionMessage && (
                <Typography variant="body1" sx={{ marginTop: 3, color: submissionMessage.includes('successfully') ? green[500] : red[500] }}>
                    {submissionMessage}
                </Typography>
            )}
        </Container>
    );
};

export default QuizPage;
