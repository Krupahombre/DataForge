import styles from "../../styles/Home.module.css";

const SquareBox = (props) => {
  const { changeSelectedState, selectedState, columnName } = props;

  const color = selectedState ? "green" : "rgb(62, 99, 158)";

  const handleClick = () => {
    changeSelectedState(columnName);
  };

  return (
    <div
      className={styles.squareBox}
      style={{ backgroundColor: color }}
      onClick={handleClick}
    >
      <h1>{columnName}</h1>
    </div>
  );
};

export default SquareBox;
