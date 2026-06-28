export function generateQuestion(list) {
    const correct = list[Math.floor(Math.random() * list.length)];

    const wrongs = list
        .filter(p => p.name !== correct.name)
        .sort(() => Math.random() - 0.5)
        .slice(0, 3);

    return {
        correct,
        options: [...wrongs, correct].sort(() => Math.random() - 0.5)
    };
}