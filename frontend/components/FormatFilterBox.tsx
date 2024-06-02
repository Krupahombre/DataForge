import styles from "../styles/Home.module.css";

const SquareBox = (props) => {
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
