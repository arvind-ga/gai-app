import React from "react";
import {Grid} from "@mui/material";
import TermsAndPolicies from "@/sections/terms/terms-policies";

export default function Policies() {
    return (
        <div>
            <Grid container justifyContent="center" alignItems="center">
                    <TermsAndPolicies/>
            </Grid>
        </div>
    );
}
