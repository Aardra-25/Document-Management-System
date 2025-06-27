import * as React from 'react';
import Button from '@mui/material/Button';
import DeleteIcon from '@mui/icons-material/Delete';
import Stack from '@mui/material/Stack';

export default function Buttons() {
  const handleDelete = () => {
    console.log("Delete button clicked");
  };

  return (
    <Stack direction="row" spacing={2}>
      <Button variant="outlined" startIcon={<DeleteIcon />} onClick={handleDelete}>
        Delete
      </Button>
    </Stack>
  );
}
