import styles from "../styles/Home.module.css";
import React from "react";

interface ISquareBoxProps {
  changeSelectedState: (columnName: string) => void;
  selectedState: boolean;
  columnName: string;
}

const SquareBox: React.FC<ISquareBoxProps> = (props) => {
  const { changeSelectedState, selectedState, columnName } = props;

  const color = selectedState ? "#003249" : "#007EA7";

  const handleClick = () => {
    changeSelectedState(columnName);
  };

  return (
    <div
      className={styles.squareBox}
      style={{ backgroundColor: color }}
      onClick={handleClick}
    >
      <h3>{columnName}</h3>
    </div>
  );
};

export default SquareBox;
