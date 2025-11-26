import './globals.css';

export const metadata = {
  title: '360 Relationship Intelligence',
  description: 'Relationship intelligence dashboard for 360 Social Impact Studios',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
