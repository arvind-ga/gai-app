import React from "react";
import useAuthenticatedRoute from "@/hooks/use-authenticated-route";
import {Typography} from "@mui/material";
import BookingPage from "@/sections/bookings/session-bookings";


function Bookings() {
    return (
        <>
            <Typography component="h1" variant="h4" gutterBottom>
                Session Bookings
            </Typography>
            <BookingPage/>
        </>
    );
}

export default useAuthenticatedRoute(Bookings);
