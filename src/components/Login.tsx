import React from 'react'
import { FlipWords } from './ui/word-flip';
import { flipWords } from '@/data/data';
import { WavyBackground } from './ui/wavy-bg';

const LoginPage = () => {
  const handleLogin = async () => {
    try {
      const response = await fetch('http://localhost:8080/auth/login');
      const data = await response.json();
      if (data.auth_url) {
        window.location.href = data.auth_url;
      } else {
        throw new Error("Failed to get auth URL");
      }
    } catch (error) {
      console.error("Login failed:", error);
    }
  }

  return (
    <>
      <WavyBackground>
        <div className="flex flex-col items-center justify-center min-h-screen w-full text-center px-4">
          <div className="mb-6 text-white text-9xl font-bold">
            STREAMLINE
          </div>
          <div className="text-4xl text-center mb-5 font-normal text-white whitespace-nowrap">
            Music that is more <br></br>
            <FlipWords 
              words={flipWords}
              className="text-green-300 font-bold"
            />
          </div>
          <button 
            className="px-12 py-4 mb-8 rounded-full bg-[#1ED760] font-bold text-white tracking-widest uppercase transform hover:scale-105 hover:bg-[#21e065] transition-colors duration-200"
            onClick={handleLogin}
          >
            Login
          </button>
        </div>
      </WavyBackground>
    </>
  );
}

export default LoginPage