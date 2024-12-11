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

    const { accessToken } = useAuth();
    const [responses, setResponses] = useState({});
    const [submissionMessage, setSubmissionMessage] = useState('');
    const [quiz, setQuiz] = useState(null);

    const {
        data: user,
        isLoading: isUserLoading,
        isError: isUserError,
    } = useQuery('userProfile', () => getProfile(accessToken), {
        enabled: !!accessToken,
    });

    console.log("Fetching quiz with quiz id", quiz_id);
    const {
        data: quizData,
        isLoading: isQuizLoading,
        isError: isQuizError,
    } = useQuery(['quiz', quiz_id], () => fetchQuiz(quiz_id), {
        enabled: !!quiz_id,
        onSuccess: (data) => setQuiz(data),
    });
    console.log("Fetched quiz with quiz id", quiz_id);

    const handleSubmit = async () => {
        if (!quiz || Object.keys(responses).length < quiz.questions.length) {
            alert('Please answer all questions before submitting.');
            return;
        }

        const submissionData = {
            username: user?.username || '',
            email: user?.email || '',
            user_id: user?._id || '',
            mobile_number: user?.mobile_number || '',
            quizId: quiz?.id || quiz_id,
            responses,
        };

        try {
            const result = await submitQuizResponse(submissionData);
            setSubmissionMessage('Quiz submitted successfully!');
            console.log('Submission successful:', result);
        } catch (error) {
            console.error('Error submitting quiz response:', error);
            setSubmissionMessage('Failed to submit quiz. Please check your answers or try again.');
        }
    };

    if (isUserLoading || isQuizLoading) return <Loading />;
    if (isUserError || isQuizError) return <Typography>Error loading data.</Typography>;

    return (
        <Container maxWidth="md" sx={{ marginTop: 5 }}>
            {/* User Details Card */}
            <Card sx={{ mb: 4, borderRadius: '16px', boxShadow: 3, padding: 3 }}>
                <CardHeader
                    title={<Typography variant="h4">Quiz: {quiz?.id || "Loading..."}</Typography>}
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
            <Card sx={{ borderRadius: '16px', boxShadow: 3 }}>
                <CardHeader
                    title={<Typography variant="h4">Quiz Questions</Typography>}
                />
                <CardContent>
                    {quiz.questions.map((question) => (
                        <Box
                            key={question.id}
                            sx={{
                                marginBottom: 4,
                                padding: 4,
                                border: '1px solid #e0e0e0',
                                borderRadius: '8px',
                                backgroundColor: '#f9f9f9',
                            }}
                        >
                            <Typography variant="h6" sx={{ marginBottom: 2 }}>
                                {question.question}
                            </Typography>
                            <RadioGroup
                                value={responses[question.id] || ''}
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
