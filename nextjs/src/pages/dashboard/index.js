import React from 'react';
import {useRouter} from 'next/router';
import Person from '@mui/icons-material/Person';
import AccountCircle from '@mui/icons-material/AccountCircle'; // Profile Icon
import Payment from '@mui/icons-material/Payment'; // Payment Icon
import School from '@mui/icons-material/School'; // Exam Tests Icon
import Assessment from '@mui/icons-material/Assessment'; // Exam Report Icon
import CloudDownload from '@mui/icons-material/CloudDownload'; // Download Icon
import PsychologyAltIcon from '@mui/icons-material/PsychologyAlt'; //Guide Icon
import DuoIcon from '@mui/icons-material/Duo';
import ListItemButton from '@mui/material/ListItemButton';
import {Box, Button, Grid, Paper, Typography} from '@mui/material';
import popover from '@mui/material/Popover';
import Avatar from '@mui/material/Avatar';
import SettingsIcon from '@mui/icons-material/Settings';
import ButtonBase from '@mui/material/ButtonBase';
import Divider from '@mui/material/Divider';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import LogoutButton from "@/sections/auth/logout";
import { useAuth } from '@/api/auth/auth-context';
import { usePopover } from '@/hooks/use-popover';
import {checkReportExist, downloadReport} from "@/api/endpoints";

import {
    CartesianGrid,
    Cell,
    Legend,
    Line,
    LineChart,
    Pie,
    PieChart,
    ResponsiveContainer,
    Tooltip,
    BarChart,
    Bar,
    XAxis,
    YAxis
} from 'recharts';
import useAuthenticatedRoute from "@/hooks/use-authenticated-route.js";
import QuizLinks from "@/sections/quizzes/quiz-links";

export const SettingsPopover = ({ anchorEl, onClose, open }) => {
  const { userProfile } = useAuth();

  return (
    <Popover
      anchorEl={anchorEl}
      anchorOrigin={{
        vertical: "bottom",
        horizontal: "right",
      }}
      onClose={onClose}
      open={open}
      PaperProps={{ sx: { width: 200 } }}
    >
      <Box sx={{ p: 2 }}>
        <Typography variant="body1">{userProfile?.full_name}</Typography>
        <Typography color="text.secondary" variant="body2">
          {userProfile?.email}
        </Typography>
      </Box>
      <Divider />
      <Box sx={{ p: 1, display: "flex", justifyContent: "center" }}>
        <LogoutButton />
      </Box>
    </Popover>
  );
};

export const SettingsButton = () => {
  const popover = usePopover();

  return (
    <>
      <Box
        component={ButtonBase}
        onClick={popover.handleOpen}
        ref={popover.anchorRef}
        sx={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          width: 48,
          height: 48,
        }}
      >
        <Avatar sx={{ width: 36, height: 36, bgcolor: "primary.main" }}>
          <SettingsIcon sx={{ color: "white" }} />
        </Avatar>
      </Box>
      <SettingsPopover
        anchorEl={popover.anchorRef.current}
        onClose={popover.handleClose}
        open={popover.open}
      />
    </>
  );
};



const Dashboard = () => {

    const router = useRouter();

    const handleNavigation = () => {
        router.push('/user-profile');
    };

    const { userProfile, accessToken } = useAuth();
    const handleReportDownload = async () => {
      try {
        const reportExists = await checkReportExist(userProfile?.username, accessToken);
  
        if (reportExists) {
          await downloadReport(userProfile?.username, accessToken);
          toast.success("Your report is being downloaded.");
        } else {
          toast.error("Report does not exist. Please complete the test to generate your report.");
        }
      } catch (error) {
        toast.error("An error occurred while checking the report.");
        console.error("Error checking report existence:", error);
      }
    };

    const stats = [
        {label: '1. Complete/Update Profile', value: 12},
        {label: '2. Tests & Report', value: 87},
        // {label: '3. Top Recommendation', value: 5},
        {label: '3. Session Bookings', value: 5}];

    // Personality data
    const data = [
        {name: 'ENFJ', personality_score: 11},
        {name: 'ENFP', personality_score: 13},
        {name: 'ENTJ', personality_score: 5},
        {name: 'ENTP', personality_score: 9},
        {name: 'ESFJ', personality_score: 5.5},
        {name: 'ESFP', personality_score: 2.5},
        {name: 'ESTJ', personality_score: 1.5},
        {name: 'ESTP', personality_score: 5},
        {name: 'INFJ', personality_score: 12},
        {name: 'INFP', personality_score: 2.5},
        {name: 'INTJ', personality_score: 3},
        {name: 'INTP', personality_score: 8},
        {name: 'ISFJ', personality_score: 4},
        {name: 'ISFP', personality_score: 15},
        {name: 'ISTJ', personality_score: 4},
        {name: 'ISTP', personality_score: 3},
        // Add more months as needed
    ];

    const pieData = [
        {name: 'Quantitative', value: 400},
        {name: 'Logical', value: 300},
        {name: 'Situation', value: 300},
        {name: 'Verbal', value: 200},
    ];

    const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

    return (
        <>
            <Typography component="h1" variant="h4" gutterBottom>
                Dashboard
            </Typography>
            <Typography variant="h6" gutterBottom>
                Welcome back, <Typography variant="h6" component="span"
                                          color={"primary"}> {userProfile?.full_name || 'User'}!</Typography>
            </Typography>
            <Grid container spacing={3} sx={{ mt: 2 }}>
            {stats.map((stat, index) => (
                <Grid item xs={12} sm={6} md={4} key={index}>
                    <ListItemButton
                        onClick={() => {
                            if (index === 0) router.push('/user-profile');
                            else if (index === 1) router.push('/quiz-links');
                            else if (index === 2) router.push('/bookings');
                        }}
                        sx={{
                            p: 2,
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                            height: '100%',
                            borderRadius: 2,
                        }}
                    >
                        <Typography component="h2" variant="h6" color="primary" gutterBottom>
                            {stat.label}
                        </Typography>
                        <Typography component="p" variant="h4">
                            {index === 0 && <AccountCircle fontSize="large" color="primary" />}
                            {index === 1 && <Assessment fontSize="large" color="primary" />}
                            {index === 2 && <DuoIcon fontSize="large" color="primary" />}
                            {/* {index === 2 && <CloudDownload fontSize="large" color="primary" />} */}
                            
                        </Typography>
                    </ListItemButton>
                </Grid>
            ))}
        </Grid>

        
            {/* Line Chart Section */}
            <Grid container sx={{ mt: 6 }}>
                <Typography component="h1" variant="h4" gutterBottom>
                Sample Report
                </Typography>
                    <Grid item xs={12} sx={{ mt: 2 }}>
                    <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: '100%'  }}>
                    <Typography component="h2" variant="h6" color="primary" gutterBottom>
                        Personality Analysis
                    </Typography>
                    <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Bar dataKey="personality_score">
                        {data.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                            ))}
                    </Bar>
                    </BarChart>
                    </ResponsiveContainer>
                    </Paper>
                    </Grid>

</Grid>

                {/* Pie Chart Section */}
                <Grid item xs={12} sx={{ mt: 2 }}>
                    <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: '100%' }}>
                    <Typography component="h2" variant="h6" color="primary" gutterBottom>
                        Aptitude Analysis
                    </Typography>
                    <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={pieData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="name" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="value" fill="#8884d8">
                            {pieData.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                                ))}
                        </Bar>
                    </BarChart>
                    </ResponsiveContainer>
                    </Paper>
                </Grid>

            <Box sx={{display: 'flex', justifyContent: 'center', mx: 3, mt: 4, textAlign: 'center'}}>
                <Typography variant="body2" color="warning.main">
                    The information displayed is sample report, complete the test to get your personal assessment report.
                </Typography>
            </Box>

            {/* <Box sx={{display: 'flex', justifyContent: 'center', mt: 4}}>
                <Button variant="contained" color="primary"
                        onClick={() => alert('complete quizzes to get your personal assessment report')}>
                    Generate Your Report
                </Button>
            </Box> */}
        </>
    );
}; 

export default useAuthenticatedRoute(Dashboard);