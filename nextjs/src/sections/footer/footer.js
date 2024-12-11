import React from 'react';
import WhatsAppIcon from '@mui/icons-material/WhatsApp'
import YouTubeIcon from '@mui/icons-material/YouTube'
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import TwitterIcon from '@mui/icons-material/Twitter';
import InstagramIcon from '@mui/icons-material/Instagram';
//import GitHubIcon from "@mui/icons-material/GitHub";
//import CoffeeIcon from '@mui/icons-material/Coffee';
import {Box, IconButton, Link, Tooltip, Typography, useTheme} from '@mui/material';
import {InfinityG} from "@/theme/menu-icons";

const Footer = () => {
    const theme = useTheme();
    const currentYear = new Date().getFullYear();

    return (
        <Box
            component="footer"
            sx={{
                zIndex: 1,
                py: 2,
                px: 3,
                mt: 'auto',
                color: theme.palette.text.secondary,
                textAlign: 'center',
                // backgroundColor: theme.palette.background.default,
            }}
        >
            <Typography variant="body1">
                © Copyright {currentYear} |
                <Link
                    href="https://gakudoai.com"
                    target="_blank"
                    rel="noopener noreferrer"
                    underline="none"
                    color="inherit"
                    sx={{mx: 0.5}}
                >
                    GakudoAI
                </Link>
            </Typography>
            <Box sx={{mt: 1}}>

                <Tooltip title="LinkedIn">
                    <IconButton
                        component="a"
                        href="https://linkedin.com/company/gakudoai"
                        target="_blank"
                        rel="noopener noreferrer"
                        size="small"
                        sx={{p: 0.3, m: 0}}
                    >
                        <LinkedInIcon/>
                    </IconButton>
                </Tooltip>

                <Tooltip title="WhatsApp">
                    <IconButton
                        component="a"
                        href="https://wa.me/918273924386"
                        target="_blank"
                        rel="noopener noreferrer"
                        size="small"
                        sx={{p: 0.3, m: 0}}
                    >
                        <WhatsAppIcon/>
                    </IconButton>
                </Tooltip>

                <Tooltip title="YouTube">
                    <IconButton
                        component="a"
                        href="https://www.youtube.com/@gakudoai"
                        target="_blank"
                        rel="noopener noreferrer"
                        size="small"
                        sx={{p: 0.3, m: 0}}
                    >
                        <YouTubeIcon/>
                    </IconButton>
                </Tooltip>

                <Tooltip title="Instagram">
                    <IconButton
                        component="a"
                        href="https://instagram.com/gakudoai"
                        target="_blank"
                        rel="noopener noreferrer"
                        size="small"
                        sx={{p: 0.3, m: 0}}
                    >
                        <InstagramIcon/>
                    </IconButton>
                </Tooltip>

                <Tooltip title="Twitter">
                    <IconButton
                        component="a"
                        href="https://x.com/GakudoAI"
                        target="_blank"
                        rel="noopener noreferrer"
                        size="small"
                        sx={{p: 0.3, m: 0}}
                    >
                        <TwitterIcon/>
                    </IconButton>
                </Tooltip>
            </Box>
            <Typography sx={{mt: 1}}><InfinityG height={26} width={26} fill={"#9cedff"}/></Typography>
        </Box>
    );
};

export default Footer;
