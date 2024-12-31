import axios from "axios";
import {jsonHeader, staticBearerHeader} from "@/api/headers";
import dayjs from 'dayjs';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export const apiClient = axios.create({
    baseURL: API_BASE_URL,
});

// Function to log-in and get token
export const getToken = async (username, password) => {
    const response = await axios.post(`${API_BASE_URL}/token?username=${username}&password=${password}`, null, {
        headers: jsonHeader
    });
    return response.data;
};

// Function to get user profile
export const getProfile = async (accessToken) => {
    const response = await axios.get(`${API_BASE_URL}/users/profile`, {
        headers: jsonHeader(accessToken),
    });
    return response.data;
};

// log out function
export const logout = async (accessToken) => {
    await axios.post(`${API_BASE_URL}/logout`, {}, {headers: jsonHeader(accessToken)});

};


// Users related functions, get, post, delete, put
export const fetchUsers = async (accessToken) => {
    const {data} = await axios.get(`${API_BASE_URL}/users/`, {
        headers: jsonHeader(accessToken)
    });
    return data;
};

// Users related functions, get, post, delete, put
export const fetchUser = async (user, accessToken) => {
    const {data} = await axios.get(`${API_BASE_URL}/users/${user._id}`, {
        headers: jsonHeader(accessToken)
    });
    return data;
};

export const updateUser = async (user, accessToken) => {
    // noinspection JSUnresolvedReference
    const {data} = await axios.put(`${API_BASE_URL}/users/${user._id}`, user, {
        headers: jsonHeader(accessToken)
    });
    return data;
};

export const deleteUser = async (id, accessToken) => {
    await axios.delete(`${API_BASE_URL}/users/${id}`, {
        headers: jsonHeader(accessToken)
    });
    return id;
};

export const createUser = async (user, accessToken) => {
    console.log(user)
    const {data} = await axios.post(`${API_BASE_URL}/users/`, user, {
        headers: jsonHeader(accessToken)
    });
    return data;
};


// ChatGPT
export const fetchChatResponse = async (question, accessToken, model, username) => {
    console.log("Username:", username, "with AccessToken", accessToken);
    console.log("Sending question to the API:", question, "with model", model);

    const url = new URL(`${API_BASE_URL}/chat/`);
    url.searchParams.append('question', question);
    url.searchParams.append('model', model);
    url.searchParams.append('username', username); // Add username here

    const response = await fetch(url, {
        method: "GET",
        headers: {
            'accept': 'application/json',
            'api-key': accessToken, // Proper API key for authorization
        },
    });

    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
};


export const forgotPassword = async (email) => {
    try {
        const response = await axios.post(
            `${API_BASE_URL}/users/forgot-password/`,
            {}, // No body data
            {
                params: { email }, // Query parameter
                headers: staticBearerHeader, // Ensure this header is correctly defined
            }
        );
        console.log("Response:", response);
    } catch (error) {
        console.error("Error:", error);
        console.error("Error Response:", error.response); // Check the response details
        console.error("Error Request:", error.request);   // Check the raw request
    }
};


export const postResetPassword = async ({token, newPassword}) => {
    const response = await axios.post(`${API_BASE_URL}/users/reset-password/`, {}, {
        params: {token, new_password: newPassword},
        headers: staticBearerHeader,
    });
    return response.data;
};


export const postRegister = async (userData) => {
    console.info("inside postRegister frontend endpoint function", userData)
    const response = await axios.post(`${API_BASE_URL}/register/`, {
        email: userData.email,
        full_name: userData.fullName,
        password: userData.password,
        username: userData.username,
        standard: userData.standard,
    }, {
        headers: staticBearerHeader,
    });

    return response.data;
};

// mail settings
export const fetchMessageSettings = async (accessToken) => {
    // Pass the accessToken directly to use it in the request
    const {data} = await apiClient.get('config', {
        headers: jsonHeader(accessToken)
    });
    return data;
};

export const updateMessageSettings = async ({section, settings, accessToken}) => {
    // Include accessToken in the request
    await apiClient.put(`config`, {[section]: settings}, {
        headers: jsonHeader(accessToken)
    });
    return settings;
};


export const emailQuery = async (name, email, mobile, subject, body) => {
    console.log("Query being sent:", name, email, mobile, subject, body);
    try {
        const response = await axios.post(`${API_BASE_URL}/query/`,
            {}, // Empty body
        {
        params: { name, email, mobile, subject, body },
            }
        );
        console.log("Query sent:", response.data);
        return response.data;
    } catch (error) {
        console.error("Error while sending query mail", error);
        throw error;
    }
};

export const fetchQuiz = async (quiz_id, user_id, accessToken) => {
    try {
        const url = `${API_BASE_URL}/quiz/`;
        console.log(`Making GET request to: ${url}`);  // Log the URL

        const response = await axios.get(url,
            {
            params: { quiz_id, user_id }, // Send user_id as query parameter
            headers: { 'accept': 'application/json', 'api-key': accessToken },
                }
            );
        console.log("Received quiz data:", response.data);  // Log response data
        return response.data;
    } catch (error) {
        console.error("Error fetching quiz:", error.response?.data || error.message);  // Log error details
        throw error;
    }
};

export const checkQuizResponseExist = async (quiz_id, user_id, accessToken) => {
    try {
        const url = `${API_BASE_URL}/check-quiz-response-exist/`;
        console.log(`Making GET request to: ${url}`);  // Log the URL

        const response = await axios.get(url,
            {
            params: { quiz_id, user_id }, // Send user_id as query parameter
            headers: { 'accept': 'application/json', 'api-key': accessToken },
                }
            );
        console.log("Received quiz data:", response.data);  // Log response data
        return response.data;
    } catch (error) {
        console.error("Error fetching quiz:", error.response?.data || error.message);  // Log error details
        throw error;
    }
};


// Submit quiz response
export const submitQuizResponse = async (responseData, accessToken) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/save-quiz-response/`, responseData, {
            headers: { 'accept': 'application/json', 'api-key': accessToken }
        });
        return response.data;
    } catch (error) {
        console.error("Error submitting quiz response:", error);
        throw error;
    }
};


// Generate Report
export const checkReportExist = async (user_id, accessToken) => {
    try {
        console.log("User ID:", user_id);
        console.log("Access token:", accessToken);


        if (!user_id) throw new Error("user_id is required");
        if (!accessToken) throw new Error("Access token is required");

        const response = await axios.get(`${API_BASE_URL}/check-report-exist/`, {
            params: { user_id }, // Send user_id as query parameter
            headers: { 'accept': 'application/json', 'api-key': accessToken },
        });

        console.log("Checking report exists or not js:", response.data);
        return response.data;
    } catch (error) {
        console.error("Please complete all the quiz:", error);
        throw error;
    }
};

// Generate Report
export const GenerateReport = async (user_id, accessToken) => {
    try {
        console.log("User ID:", user_id);
        console.log("Access token:", accessToken);

        if (!user_id) throw new Error("user_id is required");
        if (!accessToken) throw new Error("Access token is required");
        // const encodedUserId = encodeURIComponent(user_id);

        const response = await axios.post(`${API_BASE_URL}/generate-report/`,
            {}, // Empty body
        {
        params: { user_id }, // Send user_id as query parameter
        headers: { 'accept': 'application/json', 'api-key': accessToken },
            }
        );
        console.log("Please is being generated js:", response.data);
        return response.data;
    } catch (error) {
        console.error("Please complete all the quiz:", error);
        throw error;
    }
};

export const downloadReport = async (user_id, accessToken) => {
    try {
        // Fetch the download link from the backend
        console.log(`user_id: ${user_id}`);
        console.log(`accessToken: ${accessToken}`);
        const url = `${API_BASE_URL}/report-download-link/`;
        console.log(`Making GET request to: ${url}`);  // Log the URL
        const response = await axios.get(url,
    {
        params: { "user_id":user_id }, // Send user_id as query parameter
        headers: { 'accept': 'application/json', 'api-key': accessToken },
    }
        );
//        const response = await getReportDownloadLink(id);

        if (response?.data) {
            console.log("Redirecting to download URL:", response.data.url);
            // Trigger file download by navigating to the URL
            window.location.href = response.data.url;
        } else {
            alert("No URL found in the response.");
            console.error("Response did not contain a valid URL:", response);
        }
    } catch (error) {
        alert("Error, Report not generated. Please complete test and generate report then try again.");
        console.error("Error in downloading report:", error);
    }
};

// Fetching Booking
export const fetchBooking = async (username, accessToken) => {
    try {
        if (!username) throw new Error("username is required");
        if (!accessToken) throw new Error("Access token is required");

        const response = await axios.get(`${API_BASE_URL}/fetch-booking/`, {
            params: { username }, // Corrected query parameter name
            headers: { 'accept': 'application/json', 'api-key': accessToken },
        });
        console.log("Got response from fetchBooking:", response)
        // Extract and return the booking_list
        // Extract and return the booking_list
        const bookingList = response.data?.booking_list; // Corrected path
        if (!Array.isArray(bookingList)) {
            throw new Error("Invalid response structure from API.");
        }
        return bookingList;
    } catch (error) {
        console.error("Error fetching bookings:", error);
        throw error;
    }
};

// Session Booking
export const SessionBooking = async (username, dateTime, remark, accessToken) => {
    try {
        console.log("Inside SessionBooking endpoint")
        if (!username || !dateTime || !remark) throw new Error("All fields are required");
        if (!accessToken) throw new Error("Access token is required");

        const response = await axios.post(`${API_BASE_URL}/booking/`, {
            username,
            dateTime: dayjs(dateTime).toISOString(), // Ensure ISO format
            remark,
        }, {
            headers: { 'accept': 'application/json', 'api-key': accessToken },
        });
        return response.data;
    } catch (error) {
        console.error("Error creating booking:", error);
        throw error;
    }
};