import React from "react";
import ColumnFilterBox from "./ColumnFilterBox";
import styles from "../styles/Home.module.css";
import IFiltersProps from "../common/models/IFilterProps";

const ColumnFilters: React.FC<IFiltersProps> = ({ filters, setFilters }) => {
  const handleToggle = (key: number) => {
    const newFilters = [...filters];
    newFilters[key] = {
      ...newFilters[key],
      selected: !newFilters[key].selected,
    };
    setFilters(newFilters);
  };

  return (
    <div className={styles.chooseFilterWrapper}>
      <h1 className={styles.chooseFiltersLabel}>Choose the types of data:</h1>
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

export default ColumnFilters;
