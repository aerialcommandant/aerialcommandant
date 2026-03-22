"""Small dataframe utilities."""

from __future__ import annotations


def remove_outliers_manual(df, column):
    """Return rows whose values fall within three standard deviations of the mean.

    Args:
        df: A pandas DataFrame-like object.
        column: Name of the numeric column to filter.

    Returns:
        A filtered dataframe containing only rows whose values in ``column`` are
        within the inclusive range ``mean ± 3 * std``.
    """
    mean = df[column].mean()
    std = df[column].std()

    return df[(df[column] >= mean - 3 * std) & (df[column] <= mean + 3 * std)]
