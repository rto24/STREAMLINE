export interface UserContextInterface {
  username: string | null,
  setUsername: React.Dispatch<React.SetStateAction<string | null>>;
}

export interface GeneratedSongInterface {
  id: string,
  artist: string,
  name: string,
  url: string,
  duration: number,
  img: string,
  album: string,
}

export interface SongCardInterface {
  id: string,
  artist: string,
  name: string,
  img: string,
  ctaText1: string,
  ctaText2: string,
  ctaLink: string
}

export interface SavedSongInterface {
  id: string,
  artist: string,
  name: string,
  img: string,
  ctaText1?: string,
  ctaText2?: string,
  ctaLink: string,
}

export interface PlaylistProps {
  initialItems: SavedSongInterface[],
}