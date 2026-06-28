import { useEffect, useState } from "react";
import { generateQuestion } from "./utils/game";

import ScoreHeader from "./components/ScoreHeader";
import QuestionCard from "./components/QuestionCard";
import OptionButton from "./components/OptionButton";

export default function App() {
    const [data, setData] = useState([]);
    const [question, setQuestion] = useState(null);
    const [options, setOptions] = useState([]);
    const [status, setStatus] = useState("idle");
    const [score, setScore] = useState(0);
    const [streak, setStreak] = useState(0);

    useEffect(() => {
        fetch("/data/performers.json")
            .then(r => r.json())
            .then(json => {
                setData(json);
                const q = generateQuestion(json);
                setQuestion(q.correct);
                setOptions(q.options);
            });
    }, []);

    function nextQuestion(list = data) {
        const q = generateQuestion(list);
        setQuestion(q.correct);
        setOptions(q.options);
        setStatus("idle");
    }

    function handleAnswer(opt) {
        if (status !== "idle") return;

        if (opt.name === question.name) {
            setStatus("correct");
            setScore(s => s + 1);
            setStreak(s => s + 1);
        } else {
            setStatus("wrong");
            setStreak(0);
        }

        setTimeout(() => nextQuestion(), 900);
    }

    if (!question) return null;

    return (
        <div className="min-h-screen bg-[#0a0a0f] text-white flex flex-col items-center px-4 py-6">

            <ScoreHeader score={score} streak={streak} />

            <div className="w-full max-w-sm">
                <QuestionCard image={question.image} status={status} />
            </div>

            <div className="w-full max-w-sm mt-6 space-y-2">
                {options.map((opt, i) => (
                    <OptionButton
                        key={i}
                        label={opt.name}
                        status={status}
                        isCorrect={opt.name === question.name}
                        onClick={() => handleAnswer(opt)}
                    />
                ))}
            </div>
        </div>
    );
}