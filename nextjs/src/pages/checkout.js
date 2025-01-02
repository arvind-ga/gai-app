import React from "react";
import {Grid} from "@mui/material";
import { loadRazorpayScript } from '@/sections/payments/razorpay';
import CheckoutPage from '@/sections/payments/razorpay';


export default function Checkout() {
    return (
        <div>
            <Grid container justifyContent="center" alignItems="center">
                <Grid item xs={12} sm={8} md={6} lg={5}>
                    <CheckoutPage/>
                </Grid>
            </Grid>
        </div>
    );
}


// export default function Checkout() {
//     return (
//         <AuthProvider>
//             <CheckoutPage />
//         </AuthProvider>
//     );
// }


// export default function CheckoutPage() {
//     const { accessToken } = useAuth();
//     const { data: user, isLoading } = useQuery('userProfile', () => getProfile(accessToken), {
//         enabled: !!accessToken,
//     });
//     const loadAndInitializeRazorpay = async () => {
//         const isLoaded = await loadRazorpayScript('https://checkout.razorpay.com/v1/checkout.js');
//         if (!isLoaded) {
//             console.error('Failed to load Razorpay SDK');
//             return;
//         }

//         console.log('Razorpay SDK loaded');
//         if (typeof Razorpay === 'undefined') {
//             console.error('Razorpay object is not available.');
//             return;
//         } else {
//             console.log('Razorpay object found:', Razorpay);
//         }
//         if (typeof Razorpay !== 'undefined') {
//             initializeRazorpay();
//         } else {
//             console.error('Razorpay object is not available.');
//         }
//     };

//     useEffect(() => {
//         if (typeof window !== 'undefined') {
//             loadAndInitializeRazorpay();
//         }
//     }, []);

//     return (
//         <div>
//             <h1>Checkout</h1>
//             <button id="rzp-button1" aria-label="Pay Now">Pay Now</button>
//         </div>
//     );
// }
