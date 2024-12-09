"use client";
import Image from "next/image";
import React, { useEffect, useId, useRef, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { useOutsideClick } from "@/hooks/use-outside-click";
import { SavedSongInterface, SongCardInterface } from "@/types/types";

interface ExpandableCardDemoProps {
  cards: SongCardInterface[] | SavedSongInterface[];
  saveToPlaylist: (song: SongCardInterface) => void;
}

export default function ExpandableCardDemo({ saveToPlaylist, cards }: ExpandableCardDemoProps) {
  const [active, setActive] = useState<SongCardInterface | SavedSongInterface | null>(null);
  const ref = useRef<HTMLDivElement>(null);
  const id = useId();

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        setActive(null);
      }
    };

    document.body.style.overflow = active ? "hidden" : "auto";
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [active]);

  useOutsideClick(ref, () => setActive(null));

  return (
    <>
      <AnimatePresence>
        {active && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 bg-black/20 h-full w-full z-10"
          />
        )}
      </AnimatePresence>

      <AnimatePresence>
        {active && (
          <div className="fixed inset-0 grid place-items-center z-[100]">
            <motion.div
              layoutId={`card-${active.name}-${id}`}
              ref={ref}
              className="w-full max-w-[500px] h-full md:h-fit md:max-h-[90%] flex flex-col bg-white dark:bg-neutral-900 sm:rounded-3xl overflow-hidden"
            >
              <motion.div layoutId={`image-${active.name}-${id}`}>
                <Image
                  priority
                  width={1000}
                  height={1000}
                  src={active.img}
                  alt={active.name}
                  className="w-full h-80 lg:h-80 sm:rounded-tr-lg sm:rounded-tl-lg object-cover object-top"
                />
              </motion.div>

              <div>
                <div className="flex justify-between items-start p-4">
                  <div>
                    <motion.h3
                      layoutId={`title-${active.name}-${id}`}
                      className="font-bold text-neutral-700 dark:text-neutral-200"
                    >
                      {active.name}
                    </motion.h3>
                    <motion.p
                      layoutId={`description-${active.artist}-${id}`}
                      className="text-neutral-600 dark:text-neutral-400"
                    >
                      {active.artist}
                    </motion.p>
                  </div>
                  <motion.a
                    layoutId={`button-${active.name}-${id}`}
                    href={active.ctaLink}
                    target="_blank"
                    className="px-4 py-3 text-sm rounded-full font-bold bg-green-500 text-white"
                  >
                    {active.ctaText1}
                  </motion.a>
                </div>
              </div>
            </motion.div>
          </div>
        )}
      </AnimatePresence>

      <ul className="max-w-2xl mx-auto w-full gap-4 mt-2">
        {cards.map((card, idx) => (
          <motion.div
            key={`${card.name}${idx}`}
            layoutId={`card-${card.name}-${id}`}
            onClick={() => setActive(card)}
            className="p-4 flex flex-col md:flex-row justify-between items-center border-2 border-black hover:border-green-300 rounded-xl cursor-pointer dark:hover:bg-neutral-800"
          >
            <div className="flex gap-4 flex-col md:flex-row">
              <motion.div layoutId={`image-${card.name}-${id}`}>
                <Image
                  width={300}
                  height={300}
                  src={card.img}
                  alt={card.name}
                  className="h-40 w-40 md:h-14 md:w-14 rounded-lg object-cover object-top"
                />
              </motion.div>
              <div>
                <motion.h3
                  layoutId={`title-${card.name}-${id}`}
                  className="font-medium text-white dark:text-neutral-200 text-center md:text-left"
                >
                  {card.name}
                </motion.h3>
                <motion.p
                  layoutId={`description-${card.artist}-${id}`}
                  className="text-neutral-600 dark:text-neutral-400 text-center md:text-left"
                >
                  {card.artist}
                </motion.p>
              </div>
            </div>
            <div className="flex gap-5">
            <motion.button
              layoutId={`button1-${card.name}-${id}`}
              className="px-4 py-2 text-sm rounded-full font-bold bg-gray-100 hover:bg-green-500 hover:text-white text-black mt-4 md:mt-0"
            >
              {card.ctaText1}
            </motion.button>
            <motion.button
              layoutId={`button2-${card.name}-${id}`}
              className="px-4 py-2 text-sm rounded-full font-bold bg-gray-100 hover:bg-green-500 hover:text-white text-black mt-4 md:mt-0"
              onClick={(e) => {
                e.stopPropagation();
                saveToPlaylist(card);
              }}
            >
              {card.ctaText2}
            </motion.button>
            </div>
          </motion.div>
        ))}
      </ul>
    </>
  );
}