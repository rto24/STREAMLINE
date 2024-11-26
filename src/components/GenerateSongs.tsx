import React, { useState } from 'react'
import { GeneratedSongInterface } from '@/types/types'

const GenerateSongs = () => {
  const [ generatedSongs, setGeneratedSongs ] = useState<GeneratedSongInterface[]>([])

  const handleGenerateClick = async () => {
    
  }

  return (
    <div>
      <button 
        className="px-12 py-4 rounded-full bg-[#1ED760] font-bold text-white tracking-widest uppercase transform hover:scale-105 hover:bg-[#21e065] transition-colors duration-200"
        onClick={handleGenerateClick}
      >
        GENERATE SONGS
      </button>
    </div>
  )
}

export default GenerateSongs