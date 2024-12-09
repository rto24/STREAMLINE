"use client"

import React, { useState } from 'react'
import { SavedSongInterface, PlaylistProps } from '@/types/types'
import ExpandableCardDemo from './blocks/expandable-card-demo-standard'

const SavedSongs = ({ initialItems }: PlaylistProps) => {
  const [ savedSongs, setSavedSongs ] = useState<SavedSongInterface[]>(initialItems)
  console.log(savedSongs)
  return (
    //change method to have actual logic later
    <ExpandableCardDemo saveToPlaylist={() => console.log("Hello World")} cards={savedSongs} />
  )
}

export default SavedSongs