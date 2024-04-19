import React from "react";
import styles from "../styles/Home.module.css";
import ColumnFilterBox from "./ColumnFilterBox";
import IFiltersProps from "../common/models/IFilterProps";

const TypeFilters: React.FC<IFiltersProps> = ({ filters, setFilters }) => {
  const handleToggle = (key: number) => {
    const newFilters = filters.map((filter, index) => {
      return {
        ...filter,
        selected: index === key,
      };
    });
    setFilters(newFilters);
  };

  return (
    <div>
      <h1 className={styles.chooseFiltersLabel}>Choose a data format:</h1>
      <div className={styles.chooseFilterBox}>
        {filters.map((filter, key) => (
          <ColumnFilterBox
            key={key}
            columnName={filter.name}
            selectedState={filter.selected}
            changeSelectedState={() => handleToggle(key)}
          />
        ))}
      </div>
    </div>
  );
};

export default TypeFilters;
