"use client";
import { useState } from "react";
import styled from "styled-components";

const StyledAllDiv = styled.div`
  display: flex;
  border-radius: 5px;
  margin: 5px;
  width: 105px;
  height: 100px;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  color: white;
  background: ${({ isSelected, color }) => (isSelected ? "green" : color)};
  transition: background-color 0.5s;
  &:hover {
    background: rgb(85, 116, 166);
  }
  cursor: pointer;
`;

export default function SingleSquare({ title, color }) {
  const [isSelected, setIsSelected] = useState(false);

  const handleClick = () => {
    setIsSelected(!isSelected);
  };

  return (
    <StyledAllDiv isSelected={isSelected} color={color} onClick={handleClick}>
      {title}
    </StyledAllDiv>
  );
}
