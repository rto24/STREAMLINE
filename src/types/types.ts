export interface UserContextInterface {
  username: string | null,
  setUsername: React.Dispatch<React.SetStateAction<string | null>>;
}