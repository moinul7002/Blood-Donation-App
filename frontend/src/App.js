import {
  Button,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
} from "@mui/material";
import axios from "axios";
import { useEffect, useState } from "react";
import "./App.css";
import Card from "./components/card/Card";
import BasicModal from "./components/modal/Modal";

function App() {
  const [open, setOpen] = useState(false);
  const [listOpen, setListOpen] = useState(false);
  const [getdata, updateGetData] = useState();

  const [searchInput, updateSearchInput] = useState("");
  const [search, updateSearch] = useState("");

  const handleSearch = (e) => {
    updateSearchInput(e.target.value);
  };

  const changeInput = () => {
    if (searchInput.includes("+")) {
      const newPos = searchInput.replace("+", "POS");
      updateSearch(newPos);
    } else if (searchInput.includes("-")) {
      const newNeg = searchInput.replace("-", "NEG");
      updateSearch(newNeg);
    }
  };
  const onSearch = async () => {
    const res = await axios.get(
      `http://127.0.0.1:8000/api/search/?q=${search}`
    );
    updateGetData(res.data.results);
  };

  const handleClose = () => setOpen(false);

  const handleGetData = async () => {
    setListOpen(true);
    const res = await axios.get("http://127.0.0.1:8000/api/list-of-donors/");
    updateGetData(res.data.results);
  };

  useEffect(() => {
    changeInput();
  }, [searchInput]);

  return (
    <div>
      <div className="App">
        <BasicModal handleClose={handleClose} open={open} />
        <Card title="Donor" onClick={() => setOpen(true)} />
        <Card title="Recipient" onClick={handleGetData} />
      </div>
      <div className={"list-wrapper " + (listOpen ? "dBlock" : "dNone")}>
        <div
          style={{
            display: "flex",
            alighItems: "center",
            marginBottom: "20px",
          }}
        >
          <div style={{ marginBottom: "10px" }}>
            <TextField
              size="small"
              id="filled-search"
              label="Search"
              type="search"
              variant="filled"
              onChange={handleSearch}
            />
          </div>
          <div style={{ margin: "10px" }}>
            <Button onClick={onSearch}>Search</Button>
          </div>
        </div>

        {getdata?.length > 0 ? (
          <div>
            <TableContainer component={Paper}>
              <Table
                sx={{ minWidth: "100%" }}
                size="small"
                aria-label="a dense table"
              >
                <TableHead>
                  <TableRow>
                    <TableCell>Name</TableCell>
                    <TableCell align="right">Age</TableCell>
                    <TableCell align="right">Sex</TableCell>
                    <TableCell align="right">Location</TableCell>
                    <TableCell align="right">Blood Group</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {getdata?.map((data) => (
                    <TableRow
                      key={data.name}
                      sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                    >
                      <TableCell component="th" scope="row">
                        {data.firstname + " " + data.lastname}
                      </TableCell>
                      <TableCell align="right">{data.age}</TableCell>
                      <TableCell align="right">{data.sex}</TableCell>
                      <TableCell align="right">{data.location}</TableCell>
                      <TableCell align="right">{data.blood_group}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          </div>
        ) : (
          "Data Not Found."
        )}
      </div>
    </div>
  );
}

export default App;
