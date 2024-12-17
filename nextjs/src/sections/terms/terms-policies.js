import React from 'react';

const TermsAndPolicies = () => {
    return (
        <div className="container mx-auto p-6">
            <h1 className="text-3xl font-bold text-center mb-6">Privacy Policy & Terms and Conditions & Refund Policies</h1>
            
            <section className="mb-12">
                <h2 className="text-2xl font-semibold mb-4">Privacy Policies</h2>
                <p className="text-gray-700 mb-4">
                    At "GakudoAI Edutech Private Limited", we deeply value your privacy and are devoted to safeguarding your personal data. This Privacy Policy delineates the ways we gather, handle, reveal, and protect your information when you engage with our online AI-based courses or make use of our website and services. By utilizing our services, website, or enrolling in our courses, you consent to the conditions of this Privacy Policy. If you disagree with the terms provided in this Privacy Policy, we kindly ask that you refrain from accessing our website or signing up for our courses.
                </p>
                <h3 className="text-lg font-medium mb-2">Information We Gather</h3>
                <ul className="list-disc list-inside mb-4">
                    <li><strong>Personal Information:</strong> Details like name, email address, and payment information.</li>
                    <li><strong>User Information:</strong> Usage patterns, pages viewed, and time spent on the website.</li>
                    <li><strong>Device and Browser Details:</strong> IP address, browser type, and device version.</li>
                </ul>
                <h3 className="text-lg font-medium mb-2">How We Utilize Your Information</h3>
                <p className="text-gray-700 mb-4">
                    We use the collected data to provide services, communicate updates, improve user experiences, ensure security, and comply with legal requirements.
                </p>
                <h3 className="text-lg font-medium mb-2">Disclosure of Your Information</h3>
                <p className="text-gray-700 mb-4">
                    Your data may be shared with third-party providers or in compliance with legal requirements.
                </p>
                <h3 className="text-lg font-medium mb-2">Data Security</h3>
                <p className="text-gray-700 mb-4">
                    We take appropriate measures to safeguard your information but cannot guarantee absolute security.
                </p>
            </section>

            <section className="mb-12">
                <h2 className="text-2xl font-semibold mb-4">Terms & Conditions</h2>
                <p className="text-gray-700 mb-4">
                    By accessing, using, or registering an account with our Services, you acknowledge entering into a legally binding contract with "GakudoAI Edutech Private Limited" and agree to abide by these terms and our privacy policy.
                </p>
                <h3 className="text-lg font-medium mb-2">Cookies</h3>
                <p className="text-gray-700 mb-4">
                    By accessing our site, you agree to the use of cookies for enhancing user experiences and functionality.
                </p>
                <h3 className="text-lg font-medium mb-2">Content Usage</h3>
                <p className="text-gray-700 mb-4">
                    All intellectual property on this site is owned by "GakudoAI Edutech Private Limited". Users are prohibited from republishing, selling, or redistributing content without permission.
                </p>
            </section>

            <section className="mb-12">
                <h2 className="text-2xl font-semibold mb-4">Refund Policy</h2>
                <p className="text-gray-700 mb-4">
                    Our Refund Policy ensures transparency. Services are generally non-refundable and non-transferable. Refunds, if applicable, will be processed within 10-14 business days and may be provided as credit at our discretion.
                </p>
            </section>

            <section className="mb-12">
                <h2 className="text-2xl font-semibold mb-4">Contact Us</h2>
                <p className="text-gray-700">
                    For any questions or concerns, please reach out using the contact details provided on our website.
                </p>
            </section>
        </div>
    );
};

export default TermsAndPolicies;
