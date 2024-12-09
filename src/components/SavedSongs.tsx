"use client"

import React, { useState } from 'react'
import { SavedSongInterface, PlaylistProps } from '@/types/types'

const SavedSongs = ({ initialItems }: PlaylistProps) => {
  const [ savedSongs, setSavedSongs ] = useState<SavedSongInterface[]>(initialItems)
  return (
    <div>SavedSongs</div>
  )
}

export default SavedSongs