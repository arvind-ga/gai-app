import axios from "axios";
import {jsonHeader, staticBearerHeader} from "@/api/headers";

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
export const fetchChatResponse = async (question, accessToken, model) => {
    // Simulated API call
    console.log("Sending question to the API:", question, "with model", model);

    const url = new URL(`${API_BASE_URL}/chat/`);
    url.searchParams.append('question', question);
    url.searchParams.append('model', model);

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'accept': 'application/json',
            'api-key': accessToken,
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
    const response = await axios.post(`${API_BASE_URL}/register/`, {
        email: userData.email,
        full_name: userData.fullName,
        password: userData.password,
        username: userData.username,
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

export const submitQuiz = async (quizData) => {
    const response = await axios.post(`${API_BASE_URL}/submit_quiz/`, {
        quizData
    }, {
        headers: staticBearerHeader,
    });

    return response.data;
};

export const fetchQuiz = async (id) => {
    try {
        const url = `${API_BASE_URL}/quiz/${id}`;
        console.log(`Making GET request to: ${url}`);  // Log the URL
        const response = await axios.get(url);
        console.log("Received quiz data:", response.data);  // Log response data
        return response.data;
    } catch (error) {
        console.error("Error fetching quiz:", error.response?.data || error.message);  // Log error details
        throw error;
    }
};


// Submit quiz response
export const submitQuizResponse = async (responseData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/save-quiz-response`, responseData);
        return response.data;
    } catch (error) {
        console.error("Error submitting quiz response:", error);
        throw error;
    }
};


export const downloadReport = async (id) => {
    try {
        // Fetch the download link from the backend
        const url = `${API_BASE_URL}/report-download-link/${id}`;
        console.log(`Making GET request to: ${url}`);  // Log the URL
        const response = await axios.get(url);
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
        alert("Error while fetching the download link. Please try again.");
        console.error("Error in downloading report:", error);
    }
};