import React from "react";
import useAuthenticatedRoute from "@/hooks/use-authenticated-route";
import {Typography} from "@mui/material";
//import {UserProfile} from "@/sections/profile/user-profile-update";
import UserProfile from "@/sections/profile/user-profile-update";

console.log('UserProfile:', UserProfile);

function UserProfileInfo() {
    return (
        <>
            <Typography component="h1" variant="h4" gutterBottom>
                Settings
            </Typography>
            <UserProfile/>
        </>
    );
}

export default useAuthenticatedRoute(UserProfileInfo);
