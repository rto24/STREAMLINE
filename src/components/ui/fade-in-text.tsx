"use client"

import { motion } from "framer-motion"

export const FadeInEffect = ({
  words,
  className
}: {
  words: {
    text: string | null;
  }[];
  className?: string;
}) => {
  return (
    <div className={`flex flex-wrap ${className}`}>
      {words.map((word, index) => (
        <motion.span
          key={index}
          initial={{ opacity: 0, y: 10 }} 
          animate={{ opacity: 1, y: 0 }} 
          transition={{
            delay: index * 0.2,
            duration: 0.5,
            ease: "easeOut",
          }}
          className="inline-block mx-1 text-white text-2xl mb-3"
        >
          {word.text}
        </motion.span>
      ))}
    </div>
  )
}