// menuItems.js
import DashboardIcon from '@mui/icons-material/Dashboard';
import LoginIcon from '@mui/icons-material/Login';
import PeopleAltIcon from '@mui/icons-material/PeopleAlt';
import GitHubIcon from '@mui/icons-material/GitHub';
import ExtensionIcon from '@mui/icons-material/Extension';
import React from "react";
import {ChatGptIcon} from "@/theme/menu-icons";
import BusinessIcon from '@mui/icons-material/Business';

const iconStyle = {height: 16, width: 16, mb: "-3px", mr: 0.5};

export const menuItems = [
    {
        icon: <DashboardIcon sx={iconStyle}/>,
        label: "Dashboard",
        tooltip: "Dashboard Page",
        path: "/dashboard",
        authenticated: true
    },
    {
    icon: <ChatGptIcon width={20} height={20} sx={iconStyle} />, // Using ChatGPT icon directly
    label: "Ask Anything",
    tooltip: "AI Guide", // Updated tooltip to match functionality
    path: "/extensions/chatgpt", // Direct path to ChatGPT
    authenticated: true
},
    {
        icon: <BusinessIcon sx={iconStyle}/>,
        label: "About Us",
        tooltip: "README.md Documentations",
        path: "/",
        authenticated: null
    },
    {
        icon: <LoginIcon sx={iconStyle}/>,
        label: "Login",
        tooltip: "Login Page",
        path: "/login",
        authenticated: false
    },
    
];
