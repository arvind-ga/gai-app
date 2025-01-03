import React, { useState } from 'react';
import { Card, CardContent, Grid, Stack, TextField, Typography, Button, List, ListItem, ListItemText } from '@mui/material';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import { DateTimePicker, LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'; // Using Day.js as the adapter
import { useQuery, useMutation, useQueryClient } from "react-query";
import toast from "react-hot-toast";
import { useAuth } from "@/api/auth/auth-context";
import { fetchBooking, SessionBooking } from "@/api/endpoints";
import { getProfile } from "@/api/endpoints";

import {useRouter} from 'next/router';
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import localizedFormat from 'dayjs/plugin/localizedFormat';
import weekOfYear from 'dayjs/plugin/weekOfYear';
import isBetween from 'dayjs/plugin/isBetween';
import { v4 as uuidv4 } from 'uuid';

// Extend dayjs with plugins
dayjs.extend(customParseFormat);
dayjs.extend(localizedFormat);
dayjs.extend(weekOfYear);
dayjs.extend(isBetween);

const BookingPage = () => {
    const generateBookingId = (username) => {return `${username}_${uuidv4()}`;};
    const queryClient = useQueryClient();
    const { accessToken } = useAuth();
    const router = useRouter();
    const [formData, setFormData] = useState({
        username: '',
        dateTime: null,
        remark: ''
    });

    // Fetch user profile
    const { data: user, isLoading: isUserLoading, isError: isUserError } = useQuery(
        'userProfile',
        () => getProfile(accessToken),
        { enabled: !!accessToken }
    );

    // Fetch previous bookings
    const { data: bookings, isLoading: isBookingsLoading, isError: isBookingsError } = useQuery(
        ['bookings', formData.username],
        () => fetchBooking(formData.username, accessToken),
        { enabled: !!formData.username }
    );

    // Mutation for creating a new booking
    const booking_id = generateBookingId(user?.username);
    const feature = "session"

    const bookingMutation = useMutation(newBooking => SessionBooking(booking_id, newBooking.username, newBooking.dateTime, newBooking.remark, accessToken), {
        onSuccess: () => {
            toast.success('Booking created successfully!');
            queryClient.invalidateQueries(['bookings', formData.username]);
            setFormData({ ...formData, dateTime: null, remark: '' });
            router.push(`/checkout?session_booking_id=${booking_id}&feature=${feature}`); // Navigate only after success
        },
    });

    React.useEffect(() => {
        if (user?.username) {
            setFormData(prev => ({ ...prev, username: user.username }));
        } else if (!accessToken) {
            toast.error("Session expired. Please log in again.");
            router.push('/login');
        }
    }, [user, accessToken]);

    const handleFormSubmit = (e) => {
        e.preventDefault();
        const minDate = dayjs().add(1, 'day');
        if (!formData.username || !formData.dateTime || !formData.remark) {
            toast.error('All fields are required!');
            return;
        }
        if (!dayjs(formData.dateTime).isAfter(minDate, 'day')) {
            toast.error('Booking date must be at least one day in advance.');
            return;
        }
        bookingMutation.mutate(formData);
    };

    if (isUserLoading) return <Typography>Loading user data...</Typography>;
    if (isUserError) return <Typography>Error loading user data.</Typography>;

    return (
        <LocalizationProvider dateAdapter={AdapterDayjs}>
            <Stack spacing={4}>
                <Card>
                    <CardContent>
                        <Typography variant="h5" gutterBottom>Create New Booking</Typography>
                        <Grid container spacing={2} component="form" onSubmit={handleFormSubmit}>
                            <Grid item xs={12}>
                                <TextField
                                    label="Username"
                                    value={formData.username}
                                    onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                                    disabled
                                    fullWidth
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <DateTimePicker
                                    label="Date and Time"
                                    value={formData.dateTime}
                                    onChange={(newValue) => setFormData({ ...formData, dateTime: newValue })}
                                    renderInput={(params) => <TextField {...params} fullWidth />}
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    label="Remark"
                                    value={formData.remark}
                                    onChange={(e) => setFormData({ ...formData, remark: e.target.value })}
                                    fullWidth
                                />
                            </Grid>
                            <Grid item xs={12}>
                            <Button type="submit" variant="contained" color="primary">Create Booking</Button>
                            </Grid>
                        </Grid>
                    </CardContent>
                </Card>

                {/* Section for previous bookings */}
                {/* Section for previous bookings */}
                <Card>
                    <CardContent>
                        <Typography variant="h5" gutterBottom>Previous Bookings</Typography>
                        {isBookingsLoading && <Typography>Loading previous bookings...</Typography>}
                        {isBookingsError && <Typography>Error loading bookings.</Typography>}
                        {!isBookingsLoading && !isBookingsError && (
                            bookings?.length > 0 ? (
                                <TableContainer component={Paper}>
                                    <Table>
                                        <TableHead>
                                            <TableRow>
                                                <TableCell>Serial No</TableCell>
                                                <TableCell>Date and Time</TableCell>
                                                <TableCell>Remark</TableCell>
                                                <TableCell>Status</TableCell>
                                            </TableRow>
                                        </TableHead>
                                        <TableBody>
                                            {bookings.map((booking, index) => (
                                                    <TableRow key={booking.id}>
                                                        <TableCell>{index + 1}</TableCell>
                                                        <TableCell>{dayjs(booking.dateTime).format('LLL')}</TableCell>
                                                        <TableCell>{booking.remark}</TableCell>
                                                        <TableCell>
                                                            {booking.status === "Payment Pending" ? (
                                                                <Button
                                                                    variant="contained"
                                                                    onClick={() => router.push(`/checkout?session_booking_id=${booking.id}&feature=${feature}`)}
                                                                    sx={{
                                                                        backgroundColor: 'lightcoral', // Light red color
                                                                        color: '#fff', // White text
                                                                        '&:hover': {
                                                                            backgroundColor: 'indianred', // Slightly darker red on hover
                                                                        },
                                                                    }}
                                                                >
                                                                    Make Payment
                                                                </Button>
                                                            ) : booking.status === "Confirm" ? (
                                                                <Button
                                                                    variant="contained"
                                                                    disabled // Make the button unclickable
                                                                    sx={{
                                                                        backgroundColor: 'lightgreen', // Light green color
                                                                        color: '#fff', // White text
                                                                        '&:hover': {
                                                                            backgroundColor: 'lightgreen', // Maintain same color on hover
                                                                        },
                                                                    }}
                                                                >
                                                                    Confirmed
                                                                </Button>
                                                            ) : (
                                                                booking.status
                                                            )}
                                                        </TableCell>
                                                    </TableRow>
                                            ))}
                                        </TableBody>
                                    </Table>
                                </TableContainer>
                            ) : (
                                <Typography>No previous bookings found.</Typography>
                            )
                        )}
                    </CardContent>
                </Card>


            </Stack>
        </LocalizationProvider>
    );
};

export default BookingPage;