"use client"

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react'
import { UserContextInterface } from '@/types/types'

const UserContext = createContext<UserContextInterface>({
  username: null,
  setUsername: () => {},
});

const UserProvider = ({ children }: {children: ReactNode}) => {
  const [username, setUsername] = useState<string | null>(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await fetch("http://localhost:8080/auth/user", {
          credentials: "include",
        });
        if (response.ok) {
          const data = await response.json();
          setUsername(data.sub);
        } 
      } catch (error) {
        console.error('Failed to get user:', error);
      }
    }
    fetchUser();
  }, [])

  return (
    <UserContext.Provider value={{ username, setUsername }}>
      { children }
    </UserContext.Provider>
  )
}

export const useUser = () => {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error("useUser must be used within UserProvider");
  }
  return context;
}

export default UserProvider