import toast from "react-hot-toast";
import { useState, useEffect } from 'react';
import { useQuery } from 'react-query';
import {
    Avatar,
    Card,
    CardContent,
    CardHeader,
    Grid,
    IconButton,
    TextField,
    Typography,
    Select,
    MenuItem,
    FormControl,
    InputLabel,
} from '@mui/material';
import {
    Edit as EditIcon,
    Save as SaveIcon,
    Email as EmailIcon,
    AccountCircle as AccountCircleIcon,
    Badge as BadgeIcon,
    AdminPanelSettings as AdminPanelSettingsIcon,
    VerifiedUser as VerifiedUserIcon,
    Block as BlockIcon,
    School as SchoolIcon,
    Language as LanguageIcon,
    Phone as PhoneIcon,
} from '@mui/icons-material';
import { amber, blue, deepPurple, green, pink, red } from '@mui/material/colors';
import Loading from '@/components/loading';
import { getProfile, updateUser } from '@/api/endpoints';
import { useAuth } from '@/api/auth/auth-context';
import { useRouter } from 'next/router';

const standards = ["8", "9", "10", "11", "12", "Undergraduation", "Post graduation", "Job"];
const mediums = ["English"];
const streamsByStandard = {
    "8": ["All subjects"],
    "9": ["All subjects"],
    "10": ["All subjects"],
    "11": ["Arts", "Science-Maths", "Science-Bio", "Commerce", "Others"],
    "12": ["Arts", "Science-Maths", "Science-Bio", "Commerce", "Others"],
    "Undergraduation": ["Technical", "Non-technical", "Medical", "Operations", "Others"],
    "Postgraduation": ["Technical", "Non-technical", "Medical", "Operations", "Others"],
    "Job": ["Technical", "Non-technical", "Medical", "Operations", "Others"],
};

function UserProfile() {
    const { accessToken, setAccessToken } = useAuth();
    const [editMode, setEditMode] = useState(false);
    const [editedUser, setEditedUser] = useState(null);
    const [streamOptions, setStreamOptions] = useState([]);
    const router = useRouter();

    const { data: user, isLoading, isError } = useQuery(
        'userProfile',
        () => getProfile(accessToken),
        {
            enabled: !!accessToken, // Only run query if token exists
        }
    );

    useEffect(() => {
        if (user && !editedUser) {
            setEditedUser(user); // Initialize editedUser with fetched user data
            
            // Set default stream options based on standard
            let defaultStream = "";
            let defaultStreamOptions = [];
    
            // Set stream options and default based on standard
            switch (user.standard) {
                case "8":
                case "9":
                case "10":
                    defaultStream = "All subjects";  // Default for 8, 9, and 10
                    defaultStreamOptions = ["All subjects"];  // Set stream options
                    break;
                case "11":
                case "12":
                    defaultStream = "Science-Maths";  // Default for 11th and 12th
                    defaultStreamOptions = ["Arts", "Science-Maths", "Science-Bio", "Commerce", "Others"];
                    break;
                case "Undergraduation":
                case "Post graduation":
                case "Job":
                    defaultStream = "Technical";  // Default for UG, PG, and Job
                    defaultStreamOptions = ["Technical", "Non-technical", "Medical", "Operations", "Others"];
                    break;
                default:
                    defaultStream = "All subjects";  // Fallback default
                    defaultStreamOptions = ["All subjects"];
                    break;
            }
    
            setStreamOptions(defaultStreamOptions);  // Set stream options based on the standard
            setEditedUser((prevUser) => ({
                ...prevUser,
                stream: defaultStream // Set the default stream
            }));
        }
    }, [user]);

    const handleEditToggle = () => {
        setEditMode(!editMode);
    };

    const handleSave = async () => {
        try {
            const response = await updateUser(editedUser, accessToken);
            console.log('User updated successfully:', response);
            toast.success('Your profile has been updated successfully!');
            // router.push('/dashboard');
            setTimeout(() => {
                router.push('/dashboard');
            }, 1000);
            // setEditMode(false); // Exit edit mode on success
        } catch (error) {
            console.error('Error saving user data:', error);
            toast.error('There is some error while updating profile');
        }
    };

    const handleChange = (event) => {
        const { name, value } = event.target;

        // Update editedUser and dynamically adjust stream options if standard changes
        const updatedUser = { ...editedUser, [name]: value };
        if (name === "standard") {
            updatedUser.stream = ""; // Reset stream when standard changes
            setStreamOptions(streamsByStandard[value] || []);
        }
        setEditedUser(updatedUser);
    };

    if (isLoading || !user) return <Loading />;
    if (isError) return <div>Error loading user profile.</div>;

    return (
        <Card sx={{ m: 2, borderRadius: '16px', boxShadow: 3 }}>
            <CardHeader
                avatar={
                    <Avatar sx={{ bgcolor: deepPurple[500] }} aria-label="profile">
                        {user.full_name[0].toUpperCase()}
                    </Avatar>
                }
                title={<Typography variant="h6">{editMode ? 'Edit Profile' : 'Profile'}</Typography>}
                action={
                    editMode ? (
                        <IconButton aria-label="save" onClick={handleSave}>
                            <SaveIcon sx={{ color: green[500] }} />
                        </IconButton>
                    ) : (
                        <IconButton aria-label="edit" onClick={handleEditToggle}>
                            <EditIcon sx={{ color: blue[500] }} />
                        </IconButton>
                    )
                }
            />
            <CardContent>
                <Grid container spacing={2}>
                    {/*<Grid item xs={12} sm={6} display="flex" alignItems="center">
                        <BadgeIcon sx={{ color: pink[500], mr: 1 }} />
                        <Typography variant="body2">ID: {user._id}</Typography>
                    </Grid>
                    <Grid item xs={12} sm={6} display="flex" alignItems="center">
                        {user.disabled ? (
                            <BlockIcon sx={{ color: red[500], mr: 1 }} />
                        ) : (
                            <VerifiedUserIcon sx={{ color: blue[500], mr: 1 }} />
                        )}
                        <Typography variant="body2">
                            Status: {user.disabled ? 'Disabled' : 'Active'}
                        </Typography>
                    </Grid>*/}
                    <Grid item xs={12} sm={6} display="flex" alignItems="center">
                        <AccountCircleIcon sx={{ color: blue[500], mr: 1 }} />
                        {editMode ? (
                            <TextField
                                fullWidth
                                label="Full Name"
                                variant="outlined"
                                value={editedUser.full_name || ''}
                                name="full_name"
                                onChange={handleChange}
                            />
                        ) : (
                            <Typography variant="body2">Full Name: {user.full_name}</Typography>
                        )}
                    </Grid>
                    {/*<Grid item xs={12} sm={6} display="flex" alignItems="center">
                        <AccountCircleIcon sx={{ color: deepPurple[500], mr: 1 }} />
                        <Typography variant="body2">Username: {user.username}</Typography>
                    </Grid>*/}
                    <Grid item xs={12} sm={6} display="flex" alignItems="center">
                        <EmailIcon sx={{ color: green[500], mr: 1 }} />
                        {editMode ? (
                            <TextField
                                fullWidth
                                label="Email"
                                variant="outlined"
                                value={editedUser.email || ''}
                                name="email"
                                onChange={handleChange}
                            />
                        ) : (
                            <Typography variant="body2">Email: {user.email}</Typography>
                        )}
                    </Grid>
                    {/*<Grid item xs={12} sm={6} display="flex" alignItems="center">
                        <AdminPanelSettingsIcon sx={{ color: amber[700], mr: 1 }} />
                        <Typography variant="body2">Role: {user.role}</Typography>
                    </Grid>*/}
                    {/* New Fields */}
                    <Grid item xs={12} sm={6} display="flex" alignItems="center">
                        <SchoolIcon sx={{ color: amber[500], mr: 1 }} />
                        {editMode ? (
                            <TextField
                                fullWidth
                                label="School Name"
                                variant="outlined"
                                value={editedUser.school_name || ''}
                                name="school_name"
                                onChange={handleChange}
                            />
                        ) : (
                            <Typography variant="body2">School: {user.school_name}</Typography>
                        )}
                    </Grid>
                    <Grid item xs={12} sm={6} display="flex" alignItems="center">
                        <BadgeIcon sx={{ color: amber[700], mr: 1 }} />
                        {editMode ? (
                            <FormControl fullWidth variant="outlined">
                            <InputLabel id="standard-label">Standard</InputLabel>
                            <Select
                                labelId="standard-label"
                                id="standard"
                                value={editedUser.standard || ''}
                                name="standard"
                                onChange={handleChange}
                                label="Standard" // Ensures proper label behavior
                            >
                                {standards.map((standard) => (
                                    <MenuItem key={standard} value={standard}>
                                        {standard}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                        
                        ) : (
                            <Typography variant="body2">Standard: {user.standard}</Typography>
                        )}
                    </Grid>
                    <Grid item xs={12} sm={6} display="flex" alignItems="center">
                        <PhoneIcon sx={{ color: green[500], mr: 1 }} />
                        {editMode ? (
                            <TextField
                                fullWidth
                                label="Mobile Number"
                                variant="outlined"
                                value={editedUser.mobile_number || ''}
                                name="mobile_number"
                                onChange={handleChange}
                            />
                        ) : (
                            <Typography variant="body2">Mobile: {user.mobile_number}</Typography>
                        )}
                    </Grid>
                    <Grid item xs={12} sm={6} display="flex" alignItems="center">
                        <LanguageIcon sx={{ color: blue[500], mr: 1 }} />
                        {editMode ? (
                            <FormControl fullWidth variant="outlined">
                                <InputLabel id="stream-label">Stream</InputLabel>
                                <Select
                                    labelId="stream-label"
                                    id="stream"
                                    value={editedUser.stream || ''}
                                    name="stream"
                                    onChange={handleChange}
                                    label="Stream"
                                >
                                    {streamOptions.map((stream) => (
                                        <MenuItem key={stream} value={stream}>
                                            {stream}
                                        </MenuItem>
                                    ))}
                                </Select>
                            </FormControl>
                        ) : (
                            <Typography variant="body2">Stream: {user.stream}</Typography>
                        )}
                    </Grid>
                    
                </Grid>
            </CardContent>
        </Card>
    );
}

export default UserProfile;
