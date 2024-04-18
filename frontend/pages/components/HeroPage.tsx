import React, { useEffect, useState } from "react";
import styles from "../../styles/Home.module.css";
import ColumnFilters from "./ColumnFilters";
import TypeFilters from "./TypeFilters";
import IFilter from "../../common/models/IFilter";

const HeroPage = () => {
  const [columnTypes, setColumnFilters] = useState([]);
  const [typeFilters, setTypeFilters] = useState([]);

  const handleGenerate = () => {
    if (isFormFilled()) console.log("Generate button clicked");
  };

  useEffect(() => {
    setColumnFilters(getColumns());
    setTypeFilters(getTypes());
  }, []);

  const getColumns = (): IFilter[] => {
    return [
      { name: "Name", selected: false },
      { name: "LastName", selected: false },
      { name: "IBAN", selected: false },
    ];
  };

  const getTypes = (): IFilter[] => {
    return [
      { name: "JSON", selected: false },
      { name: "MySQL", selected: false },
      { name: "DUPA", selected: false },
    ];
  };

  const isFormFilled = () => {
    return (
      columnTypes.some((column) => column.selected) &&
      typeFilters.some((type) => type.selected)
    );
  };

  return (
    <div className={styles.heroBox}>
      <h1 className={styles.heroLabel}>Data Forge</h1>
      <h2 className={styles.heroSubLabel}>Generate your data!</h2>
      <div className={styles.userInputWrapper}>
        <ColumnFilters filters={columnTypes} setFilters={setColumnFilters} />
        <TypeFilters filters={typeFilters} setFilters={setTypeFilters} />
      </div>
      <div className={styles.generateBottonBox}>
        <button onClick={handleGenerate} className={styles.generateButton}>
          Generate
        </button>
      </div>
    </div>
  );
};
export default HeroPage;
