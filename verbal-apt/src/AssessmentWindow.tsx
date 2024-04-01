import { useState } from "react";
import { fetchAssessmentResponse } from "./api";

const AssessmentWindow = () => {
  const [userInput, setUserInput] = useState<string>("");
  const [convo, setConvo] = useState<string[]>([]);

  const submitInput = (input: string) => {
    setConvo([...convo, `Processing: ${input}`]);
    setUserInput("");
    fetchAssessmentResponse(input).then((response) => {
      setConvo([...convo, `You: ${input}`, `Question: ${response[0]}`]);
      console.log([response[2], response[4], response[6]]);
    });
  };

  return (
    <div>
      <h1>User Input Form</h1>
      <br />
      <div>
        {convo.map((line) => (
          <>
            <div>{line}</div>
            <br />
          </>
        ))}
      </div>
      <br />
      <label>
        Enter your input:
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
        />
      </label>
      <button onClick={() => submitInput(userInput)}>Submit</button>
    </div>
  );
};

export default AssessmentWindow;
