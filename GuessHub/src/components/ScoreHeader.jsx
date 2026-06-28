export default function ScoreHeader({ score, streak }) {
    return (
        <div className="w-full max-w-sm flex justify-between items-center mb-6">
            <div className="text-xs tracking-[0.5em] text-orange-500 uppercase font-bold">
                GuessHub
            </div>

            <div className="text-right">
                <div className="text-2xl font-black">{score}</div>
                <div className="text-[10px] text-orange-400 uppercase tracking-[0.3em]">
                    streak {streak}
                </div>
            </div>
        </div>
    );
}