import React from 'react';
import { Box, Typography, Button, Container } from '@mui/material';
import { useRouter } from 'next/router';
import Quiz from "@/sections/quizes/quiz-02";
import { fetchQuiz, submitQuizResponse } from "@/api/endpoints";

export default function QuizLinks() {
    const router = useRouter(); // Initialize the router object

    const navigateTo = (quizId) => {
    if (quizId) {
        router.push(`/quiz?id=${quizId}`);
    } else {
        console.error("Quiz ID is required to navigate");
    }
};

    return (
        <Container maxWidth="sm" sx={{ textAlign: 'center', marginTop: 5 }}>
            <Typography variant="h4" component="h1" gutterBottom>
                Assessment Quiz Links
            </Typography>
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => navigateTo('1')} // Navigate to Quiz Test 1
                    sx={{ textTransform: 'none' }}
                >
                    Quiz Test 1 (30 Min)
                </Button>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => navigateTo('2')} // Navigate to Quiz Test 2
                    sx={{ textTransform: 'none' }}
                >
                    Quiz Test 2 (30 Min)
                </Button>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => navigateTo('3')} // Navigate to Quiz Test 3
                    sx={{ textTransform: 'none' }}
                >
                    Quiz Test 3 (45 Min)
                </Button>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => navigateTo('4')} // Navigate to Quiz Test 4
                    sx={{ textTransform: 'none' }}
                >
                    Quiz Test 4 (30 Min): Optional
                </Button>
            </Box>
        </Container>
    );
}
