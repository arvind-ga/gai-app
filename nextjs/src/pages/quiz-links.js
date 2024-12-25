import React from "react";
import useAuthenticatedRoute from "@/hooks/use-authenticated-route";
import {Typography} from "@mui/material";
//import {UserProfile} from "@/sections/profile/user-profile-update";
import QuizLinks from "@/sections/quizzes/quiz-links";

function QuizLinksInfo() {
    return (
        <>
            <Typography component="h1" variant="h4" gutterBottom>
                Assessment Quizzes
            </Typography>
            <QuizLinks/>
        </>
    );
}

export default useAuthenticatedRoute(QuizLinksInfo);
