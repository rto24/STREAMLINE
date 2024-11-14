import React from 'react'

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
    <div>Login</div>
    <button 
      className="px-12 py-4 rounded-full bg-[#1ED760] font-bold text-white tracking-widest uppercase transform hover:scale-105 hover:bg-[#21e065] transition-colors duration-200"
      onClick={handleLogin}
    >
      Login
    </button>
  </>
  )
}

export default LoginPage