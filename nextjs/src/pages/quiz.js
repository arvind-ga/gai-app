import React from "react";
import useAuthenticatedRoute from "@/hooks/use-authenticated-route";
import { Typography } from "@mui/material";
import QuizPage from "@/sections/quizes/quiz-02";
import { useRouter } from "next/router";

function Quiz() {
    const router = useRouter();
    if (!router.isReady) {
        return <Typography>Loading...</Typography>;
    }

    const { id: quiz_id } = router.query; // Fetch `id` safely
    if (!quiz_id) {
        return <Typography>No quiz ID found. Please provide a valid ID.</Typography>;
    }

    return (
        <>
            <Typography component="h1" variant="h4" gutterBottom>
                Assessment Quizzes
            </Typography>
            {/* Pass only `quiz_id` to QuizPage */}
            <QuizPage quiz_id={quiz_id} />
        </>
    );
}

export default useAuthenticatedRoute(Quiz);
