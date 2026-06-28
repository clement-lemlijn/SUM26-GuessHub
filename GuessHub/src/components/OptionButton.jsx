export default function OptionButton({
                                         label,
                                         onClick,
                                         status,
                                         isCorrect
                                     }) {
    return (
        <button
            onClick={onClick}
            className={`
        w-full h-12 rounded-xl border text-sm font-medium transition-all

        ${
                status === "idle"
                    ? "bg-white/5 border-white/10 hover:border-orange-500/40 hover:bg-orange-500/10"
                    : isCorrect
                        ? "bg-orange-500/10 border-orange-500 text-orange-400"
                        : "bg-white/5 border-white/5 opacity-40"
            }
      `}
        >
            {label}
        </button>
    );
}