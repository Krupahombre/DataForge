/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [
            {
                source: '/data-generator/:path*',
                destination: 'http://backend:80/data-generator/:path*',
            },
            {
                source: '/data-generator',
                destination: 'http://backend:80/data-generator',
            }
        ];
    },
};

module.exports = nextConfig;
