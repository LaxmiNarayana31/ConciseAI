/* eslint-disable no-unused-vars */
import React from "react";

const IntroSection = () => {
  return (
    <header className="w-full flex justify-center items-center flex-col">
      <nav className="flex justify-between items-center w-full mb-10 pt-3">
        <div className="w-28 object-contain" />
        <button
          type="button"
          onClick={() =>
            window.open(
              "https://github.com/LaxmiNarayana31/ConciseAI.git",
              "_blank"
            )
          }
          className="black_btn">
          GitHub
        </button>
      </nav>

      <h1 className="head_text">
        Summarize Articles with <br className="max-md:hidden" />
        <span className="modern_gradient ">ConciseAI</span>
      </h1>
      <h2 className="desc">
        Transform lengthy articles into precise, engaging summaries with our
        open-source summarizer. Streamline your reading, spark curiosity, and
        gain a deeper understanding effortlessly.
      </h2>
    </header>
  );
};

export default IntroSection;
