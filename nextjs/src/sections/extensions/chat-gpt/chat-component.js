// ChatComponent.js
import React, {useEffect, useRef, useState} from 'react';
import {
    AppBar,
    Box,
    Button,
    Card,
    CircularProgress,
    FormControl,
    Grid,
    IconButton,
    InputLabel,
    List,
    ListItem,
    ListItemText,
    MenuItem,
    Select,
    Tab,
    Tabs,
    TextField,
    Toolbar,
    Typography
} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import {useAuth} from '@/api/auth/auth-context';
import {useRouter} from 'next/router';
import {fetchChatResponse} from "@/api/endpoints";

const saveChatsToCache = (chats) => {
    localStorage.setItem('chatConversations', JSON.stringify(chats));
};

const loadChatsFromCache = () => {
    const cachedChats = JSON.parse(localStorage.getItem('chatConversations'));
    return cachedChats || [];
};

const ChatComponent = () => {
    const {accessToken, userProfile} = useAuth();
    const [message, setMessage] = useState('');
    const [activeTab, setActiveTab] = useState(0);
    const [chats, setChats] = useState(loadChatsFromCache());
    const [model, setModel] = useState('gpt-4');
    const [isTyping, setIsTyping] = useState(false);
    const bottomRef = useRef(null);
    const [isLimitExceeded, setIsLimitExceeded] = useState(false);
    const router = useRouter();

    useEffect(() => {
        bottomRef.current?.scrollIntoView({behavior: "smooth"});
    }, [chats[activeTab]?.history]);

    useEffect(() => {
        saveChatsToCache(chats);
    }, [chats]);

    const handleSendMessage = async () => {
        if (!message.trim() || isLimitExceeded) return;

        if (chats.length === 0) {
            handleNewConversation();
            await new Promise(resolve => setTimeout(resolve, 0));
        }

        const username = userProfile?.username;
        const response = await fetchChatResponse(message, accessToken, model, username);

        if (response.isLimitExceeded === true) {
            setIsLimitExceeded(true);
            return;
        }

        console.log('Response:', response);
        console.log('isLimitExceeded:', isLimitExceeded);
        setChats(currentChats => {
            const updatedChats = [...currentChats];
            if (!updatedChats[activeTab]) {
                updatedChats.push({ history: [], model });
            }
            updatedChats[activeTab].history.push({ question: message, answer: "" });
            return updatedChats;
        });

        setIsTyping(true);

        let typedResponse = "";
        const fullResponse = response.message;
        let index = 0;

        const typingInterval = setInterval(() => {
            if (index < fullResponse.length) {
                typedResponse += fullResponse.charAt(index++);
                setChats(currentChats => {
                    const updatedChats = [...currentChats];
                    const lastMessageIndex = updatedChats[activeTab].history.length - 1;
                    updatedChats[activeTab].history[lastMessageIndex].answer = typedResponse;
                    return updatedChats;
                });
            } else {
                clearInterval(typingInterval);
                setIsTyping(false);
            }
        }, 25);

        setMessage('');
    };


    const handleNewConversation = () => {
        const newConversation = {history: [], model};
        setChats(currentChats => currentChats.length >= 20 ? [...currentChats.slice(1), newConversation] : [...currentChats, newConversation]);
        setActiveTab(chats.length >= 20 ? 19 : chats.length);
    };

    const handleChangeModel = (event) => {
        setModel(event.target.value);
    };

    const handleRedirectToPayment = () => {
        const bookingId = ""; // blank in case of chat and report
        const feature = "chat"; // payment for feature
        router.push(`/checkout?session_booking_id=${bookingId}&feature=${feature}`);
    };

    const handleDeleteChat = (index) => {
        setChats(currentChats => currentChats.filter((_, idx) => idx !== index));
        if (index === activeTab || index < activeTab) {
            setActiveTab(prev => prev > 0 ? prev - 1 : 0);
        }
    };

    return (
        <>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                        Chat Interface
                    </Typography>
                    <Button variant="contained" color="inherit" onClick={handleNewConversation} sx={{ ml: 3 }}>
                        New Conversation
                    </Button>
                </Toolbar>
            </AppBar>
            <Grid container spacing={2}>
                <Grid item xs={3}>
                    <Card sx={{ mt: 1, height: '70vh', overflow: 'auto' }}>
                        <Tabs
                            orientation="vertical"
                            variant="scrollable"
                            value={activeTab}
                            onChange={(event, newValue) => setActiveTab(newValue)}
                            aria-label="Chat tabs"
                            sx={{ borderRight: 1, borderColor: 'divider' }}
                        >
                            {chats.map((chat, index) => (
                                <Tab
                                    label={`Conversation ${index + 1}`}
                                    key={index}
                                    icon={
                                        <IconButton onClick={() => handleDeleteChat(index)} size="small">
                                            <CloseIcon fontSize="inherit" />
                                        </IconButton>
                                    }
                                    iconPosition="end"
                                />
                            ))}
                        </Tabs>
                    </Card>
                </Grid>
                <Grid item xs={9}>
                    <Card sx={{ mt: 1, height: '70vh', display: 'flex', flexDirection: 'column', position: 'relative' }}>
                        <List sx={{ overflow: 'auto', flexGrow: 1 }}>
                            {chats[activeTab]?.history.map((entry, index) => (
                                <ListItem key={index}>
                                    <ListItemText primary={`You: ${entry.question}`} secondary={`GakudoGPT: ${entry.answer}`} />
                                </ListItem>
                            ))}
                            {isTyping && <CircularProgress sx={{ alignSelf: 'center', m: 1 }} />}
                            <div ref={bottomRef} />
                        </List>
                        <Box sx={{ display: 'flex', p: 1 }}>
                            <TextField
                                fullWidth
                                label="Your question"
                                value={message}
                                onChange={(e) => setMessage(e.target.value)}
                                onKeyDown={(e) => e.key === 'Enter' && handleSendMessage()}
                                variant="outlined"
                                margin="normal"
                                disabled={isLimitExceeded}
                            />
                            <Button
                                onClick={handleSendMessage}
                                variant="contained"
                                color="primary"
                                sx={{ mt: 2, mb: 1, ml: 1 }}
                                disabled={isLimitExceeded}
                            >
                                Send
                            </Button>
                        </Box>
                        {isLimitExceeded && (
                            <Box
                            sx={{
                              position: 'absolute',
                              top: 0,
                              left: 0,
                              width: '100%',
                              height: '100%',
                              backgroundColor: 'rgba(0, 0, 0, 0.5)',
                              display: 'flex',
                              justifyContent: 'center',
                              alignItems: 'center',
                              flexDirection: 'column',
                              zIndex: 10,
                              pointerEvents: 'none', // Prevent interaction with elements beneath
                            }}
                          >
                            <Typography variant="body1" sx={{ color: 'white', mb: 1 }}>
                              Free limit exceeded. Upgrade to continue.
                            </Typography>
                            <Button
                              variant="contained"
                              color="primary"
                              onClick={handleRedirectToPayment}
                              sx={{
                                pointerEvents: 'auto', // Enable interaction with the button
                              }}
                            >
                              Go to Payment
                            </Button>
                          </Box>                                                                          
                        )}
                    </Card>
                </Grid>
            </Grid>
        </>
    );
};

export default ChatComponent;