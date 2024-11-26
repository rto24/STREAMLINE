"use client"

import React from 'react'
import { useUser } from '@/context/UserContext'
import GenerateSongs from '@/components/GenerateSongs'

const HomePage = () => {
  const { username } = useUser();
  return (
    <>
      <div>HomePage</div>
      <p>{username}</p>
      <GenerateSongs/>
    </>
  )
}

export default HomePage