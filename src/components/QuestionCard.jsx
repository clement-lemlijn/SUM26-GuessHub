import { motion, AnimatePresence } from "framer-motion";
import { Check, X } from "lucide-react";

export default function QuestionCard({ image, status }) {
    return (
        <motion.div
            className="relative rounded-2xl overflow-hidden border border-white/10 bg-black"
            animate={{
                boxShadow:
                    status === "correct"
                        ? "0 0 35px rgba(255,140,0,0.25)"
                        : status === "wrong"
                            ? "0 0 25px rgba(239,68,68,0.15)"
                            : "0 0 0px rgba(0,0,0,0)"
            }}
        >
            <img src={image} className="w-full aspect-square object-cover" />

            <AnimatePresence>
                {status !== "idle" && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className={`absolute inset-0 flex items-center justify-center
              ${status === "correct"
                            ? "bg-green-500/10"
                            : "bg-red-500/10"
                        }`}
                    >
                        {status === "correct" ? (
                            <Check className="w-20 h-20 text-green-400" />
                        ) : (
                            <X className="w-20 h-20 text-red-400" />
                        )}
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.div>
    );
}