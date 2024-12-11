import {createTheme} from "@mui/material";

export const darkTheme = createTheme({
    palette: {
        mode: 'dark',
        background: {
            default: '#0c3e8f', // Sets the default background color
        },
    },
});


export const lightTheme = createTheme({
    palette: {
        mode: 'light',
        background: {
            default: '#ffffff', // Sets the default background color to white
        },
        text: {
            primary: '#000000', // Sets the primary text color to black
        },
    },
});