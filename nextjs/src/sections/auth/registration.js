import React, {useEffect, useState} from 'react';
import { Select, MenuItem, FormControl, InputLabel } from '@mui/material'
import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    IconButton,
    TextField,
    Typography
} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import toast from "react-hot-toast";
import {useMutation} from "react-query";
import {postRegister} from "@/api/endpoints";

export default function RegistrationModal({open, handleClose}) {
    const [userData, setUserData] = useState({
        fullName: '',
        username: '',
        email: '',
        standard: '',
        password: '',
        confirmPassword: '',
    });
    const [captcha, setCaptcha] = useState('');
    const [userCaptchaInput, setUserCaptchaInput] = useState('');

    useEffect(() => {
        // Function to generate a simple captcha
        const generateCaptcha = () => {
            let result = '';
            let characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            let charactersLength = characters.length;
            for (let i = 0; i < 5; i++) {
                result += characters.charAt(Math.floor(Math.random() * charactersLength));
            }
            return result;
        };

        setCaptcha(generateCaptcha());
    }, []);

    // const handleChange = (e) => {
    //     setUserData({...userData, [e.target.name]: e.target.value});
    // };
    const handleChange = (e) => {
        const { name, value } = e.target;
    
        if (name === 'email') {
            const extractedName = value.split('@')[0];
            setUserData({
                ...userData,
                email: value,
                fullName: extractedName.charAt(0).toUpperCase() + extractedName.slice(1), // Capitalize the first letter
            });
        } else if (name === 'username') {
            const isValid = /^[a-z0-9_]*$/.test(value); // Allow only lowercase letters, numbers, and underscores
            if (isValid) {
                setUserData({ ...userData, username: value });
            } else {
                toast.error('Username can only contain lowercase letters, numbers, and underscores!');
            }
        } else {
            setUserData({ ...userData, [name]: value });
        }
    };
    
    

    const registrationMutation = useMutation(postRegister, {
        onSuccess: (data) => {
            toast.success("Successfully registered!");
            handleClose();
        },
        onError: (error) => {
            console.error('There was a problem with the registration:', error);
            toast.error("Registration failed. Please try again.");
        },
    });

    const handleRegister = () => {
        if (userData.password !== userData.confirmPassword) {
            toast.error('Passwords do not match!');
            return;
        }
        {/*if (userCaptchaInput !== captcha) {
            toast.error('Captcha does not match!');
            // Consider regenerating captcha or handling this scenario appropriately
            return;
        }*/}
        console.log("userData:", userData)

        registrationMutation.mutate(userData);
    };

    return (
        <Dialog open={open} onClose={handleClose} fullWidth maxWidth="sm">
            <DialogTitle>
                Register
                <IconButton
                    aria-label="close"
                    onClick={handleClose}
                    sx={{
                        position: 'absolute',
                        right: 8,
                        top: 8,
                        color: (theme) => theme.palette.grey[500],
                    }}
                >
                    <CloseIcon/>
                </IconButton>
            </DialogTitle>
            <DialogContent dividers>
                <TextField
                    margin="dense"
                    id="username"
                    label="Username"
                    type="text"
                    fullWidth
                    name="username"
                    variant="outlined"
                    value={userData.username}
                    onChange={handleChange}
                    sx={{mb: 2}}
                />
                <TextField
                    margin="dense"
                    id="email"
                    label="Email Address"
                    type="email"
                    fullWidth
                    name="email"
                    variant="outlined"
                    value={userData.email}
                    onChange={handleChange}
                    sx={{mb: 2}}
                />
                <FormControl fullWidth variant="outlined" sx={{ mb: 2 }}>
                    <InputLabel id="standard-label">Standard</InputLabel>
                    <Select
                        labelId="standard-label"
                        id="standard"
                        name="standard"
                        value={userData.standard}
                        onChange={handleChange}
                        label="Standard" // Ensure this matches the InputLabel text
                    >
                        <MenuItem value="8">8</MenuItem>
                        <MenuItem value="9">9</MenuItem>
                        <MenuItem value="10">10</MenuItem>
                        <MenuItem value="11">11</MenuItem>
                        <MenuItem value="12">12</MenuItem>
                        <MenuItem value="Undergraduation">Undergraduation</MenuItem>
                        <MenuItem value="Post graduation">Post Graduation</MenuItem>
                        <MenuItem value="Job">Job</MenuItem>
                    </Select>
                </FormControl>
                <TextField
                    margin="dense"
                    id="password"
                    label="Password"
                    type="password"
                    fullWidth
                    name="password"
                    variant="outlined"
                    value={userData.password}
                    onChange={handleChange}
                    sx={{mb: 2}}
                />
                <TextField
                    margin="dense"
                    id="confirmPassword"
                    label="Confirm Password"
                    type="password"
                    fullWidth
                    name="confirmPassword"
                    variant="outlined"
                    value={userData.confirmPassword}
                    onChange={handleChange}
                    sx={{mb: 2}}
                />
                {/*<Typography variant="caption" display="block" gutterBottom>
                    Captcha: {captcha}
                </Typography>
                <TextField
                    margin="dense"
                    id="userCaptchaInput"
                    label="Enter Captcha"
                    type="text"
                    fullWidth
                    variant="outlined"
                    value={userCaptchaInput}
                    onChange={(e) => setUserCaptchaInput(e.target.value)}
                    sx={{mb: 2}}
                />*/}
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose} variant="outlined" color="inherit">Cancel</Button>
                <Button onClick={handleRegister} variant="contained" color="primary">Register</Button>
            </DialogActions>
        </Dialog>
    );
}
