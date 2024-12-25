import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { Box, Button, Container, Typography, Radio, RadioGroup, FormControl, FormControlLabel, CircularProgress } from '@mui/material';
import axios from 'axios';



const quizQuestions = [
    { question: "What is the capital of France?", options: ["Paris", "Rome", "Berlin", "Madrid"], answer: "Paris" },
    { question: "Who wrote 'Hamlet'?", options: ["Shakespeare", "Hemingway", "Tolkien", "Joyce"], answer: "Shakespeare" },
    { question: "What is the boiling point of water?", options: ["100°C", "50°C", "200°C", "0°C"], answer: "100°C" },
    // Add 17 more questions below
    { question: "Which planet is known as the Red Planet?", options: ["Earth", "Mars", "Jupiter", "Venus"], answer: "Mars" },
    { question: "What is the chemical symbol for water?", options: ["H2O", "O2", "H2", "CO2"], answer: "H2O" },
    { question: "How many continents are there?", options: ["5", "6", "7", "8"], answer: "7" },
    { question: "Who painted the Mona Lisa?", options: ["Da Vinci", "Van Gogh", "Picasso", "Monet"], answer: "Da Vinci" },
    { question: "What is the largest ocean on Earth?", options: ["Atlantic", "Indian", "Arctic", "Pacific"], answer: "Pacific" },
    { question: "Which country is known as the Land of the Rising Sun?", options: ["China", "Japan", "Thailand", "Vietnam"], answer: "Japan" },
    { question: "What is the square root of 64?", options: ["6", "8", "10", "12"], answer: "8" },
    { question: "What is the speed of light?", options: ["300,000 km/s", "150,000 km/s", "200,000 km/s", "100,000 km/s"], answer: "300,000 km/s" },
    { question: "Who discovered penicillin?", options: ["Fleming", "Darwin", "Newton", "Einstein"], answer: "Fleming" },
    { question: "Which gas do plants absorb during photosynthesis?", options: ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], answer: "Carbon Dioxide" },
    { question: "Who is known as the father of computers?", options: ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], answer: "Charles Babbage" },
    { question: "What is the largest mammal?", options: ["Elephant", "Whale", "Shark", "Giraffe"], answer: "Whale" },
    { question: "What is the smallest unit of life?", options: ["Cell", "Atom", "Molecule", "Organ"], answer: "Cell" },
    { question: "What is the national sport of Japan?", options: ["Sumo", "Soccer", "Baseball", "Karate"], answer: "Sumo" },
    { question: "What is the capital of Australia?", options: ["Sydney", "Melbourne", "Canberra", "Perth"], answer: "Canberra" },
    { question: "Who developed the theory of relativity?", options: ["Newton", "Einstein", "Bohr", "Curie"], answer: "Einstein" },
    { question: "What is the chemical symbol for gold?", options: ["Au", "Ag", "Fe", "Pb"], answer: "Au" },
];

export default function QuizPage() {
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [selectedAnswer, setSelectedAnswer] = useState('');
    const [score, setScore] = useState(0);
    const [showResult, setShowResult] = useState(false);
    const {accessToken} = useAuth();
    const [editMode, setEditMode] = useState(false);
    const [editedUser, setEditedUser] = useState({});

    const {data: user, isLoading, isError} = useQuery(
        'userProfile',
        () => getProfile(accessToken),
        {
            enabled: !!accessToken, // Only run query if token exists
        }
    );

    const handleAnswerChange = (event) => {
        setSelectedAnswer(event.target.value);
    };

    const handleSubmit = () => {
        if (selectedAnswer === quizQuestions[currentQuestion].answer) {
            setScore(score + 1);
        }
        if (currentQuestion + 1 < quizQuestions.length) {
            setCurrentQuestion(currentQuestion + 1);
            setSelectedAnswer('');
        } else {
            setShowResult(true);
        }
    };

    const handleRestart = () => {
        setCurrentQuestion(0);
        setScore(0);
        setShowResult(false);
        setSelectedAnswer('');
    };

    return (
        <Container maxWidth="md" sx={{ marginTop: 5 }}>
            {showResult ? (
                <Box textAlign="center">
                    <Typography variant="h4" gutterBottom>
                        Quiz Completed
                    </Typography>
                    <Typography variant="h6">
                        Your Score: {score} / {quizQuestions.length}
                    </Typography>
                    <Button variant="contained" color="primary" onClick={handleRestart} sx={{ marginTop: 3 }}>
                        Restart Quiz
                    </Button>
                </Box>
            ) : (
                <Box>
                    <Typography variant="h5" gutterBottom>
                        Question {currentQuestion + 1} of {quizQuestions.length}
                    </Typography>
                    <Typography variant="h6" gutterBottom>
                        {quizQuestions[currentQuestion].question}
                    </Typography>
                    <FormControl component="fieldset" sx={{ marginBottom: 2 }}>
                        <FormLabel component="legend">Choose an answer:</FormLabel>
                        <RadioGroup value={selectedAnswer} onChange={handleAnswerChange}>
                            {quizQuestions[currentQuestion].options.map((option, index) => (
                                <FormControlLabel
                                    key={index}
                                    value={option}
                                    control={<Radio />}
                                    label={option}
                                />
                            ))}
                        </RadioGroup>
                    </FormControl>
                    <Box textAlign="center">
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleSubmit}
                            disabled={!selectedAnswer}
                        >
                            {currentQuestion + 1 === quizQuestions.length ? 'Finish Quiz' : 'Next Question'}
                        </Button>
                    </Box>
                </Box>
            )}
        </Container>
    );
}
