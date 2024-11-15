"use client"

import React from 'react'
import { useUser } from '@/context/UserContext'

const HomePage = () => {
  const { username } = useUser();
  return (
    <>
      <div>HomePage</div>
      <p>{username}</p>
    </>
  )
}

export default HomePage